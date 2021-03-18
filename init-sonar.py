import os
import time
from sonarqube import SonarQubeClient
from sonarqube.utils.exceptions import *
from requests.exceptions import ConnectionError
from tqdm import tqdm

url = os.getenv("SONAR_URL", "http://sonarqube:9000")
username = "admin"
default_password = "admin"
password = os.getenv("SONAR_PASSWORD", "password")
project = os.getenv("SONAR_PROJECT_KEY", "generic-project")
started = False
pbar = tqdm(desc=f"Sonar started: {started}")
while not started:
    try:
        sonar = SonarQubeClient(sonarqube_url=url, username=username, password=password)
        try:
            sonar.auth.authenticate_user(login=username, password=password)
        except AuthError as e:
            sonar = SonarQubeClient(sonarqube_url=url, username=username, password=default_password)
            sonar.auth.authenticate_user(login=username, password=default_password)
            sonar.auth.logout_user()
            sonar.users.change_user_password(username, password, default_password)
            sonar.auth.authenticate_user(login=username, password=password)
            sonar = SonarQubeClient(sonarqube_url=url, username=username, password=password)

        projects = list(sonar.projects.search_projects())

        if len(projects) == 0:
            result = sonar.projects.create_project(project, project)
        else:
            project = projects[0]["key"]

        user_tokens = sonar.user_tokens.search_user_tokens(login=username)
        if len(user_tokens["userTokens"]) == 0:
            result = sonar.user_tokens.generate_user_token(f"{project}-token")
            user_token = result["token"]
            f = open("/tmp/.env", "a")
            if project == "generic-project":
                print(project)
                print(project == "generic-project")
                f.write(f"\nSONAR_PROJECT_KEY=\"{project}\"")
            print(project)
            f.write(f"\nSONAR_PROJECT_TOKEN=\"{user_token}\"\n")
            f.close()
        started = True
        pbar.set_description(f"Sonar started: {started}")
    except (ConnectionError, ClientError, ServerError) as e:
        pbar.update(1)
        time.sleep(1)
        continue
