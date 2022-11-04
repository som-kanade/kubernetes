from jinja2 import Template, Environment, FileSystemLoader
import jinja2
import yaml


# load jinja2 template
def generateDockerfile(repoName, appName):
    templateLoader = jinja2.FileSystemLoader(searchpath="./")
    templateEnv = jinja2.Environment(loader=templateLoader)
    TEMPLATE_FILE = 'dockerFiles/Dockerfile.j2'
    template = templateEnv.get_template(TEMPLATE_FILE)

    # render dockerfile 
    dockerFileRendered = template.render(appName=appName)

    with open(repoName + '/Dockerfile', 'w') as dockerfile:
        dockerfile.write(dockerFileRendered)



    
