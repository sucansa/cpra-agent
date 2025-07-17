from crewai import Agent, Task, Crew
from dotenv import load_dotenv
import yaml

load_dotenv()

def load_yaml(file):
    with open(file, 'r') as stream:
        return yaml.safe_load(stream)

# Load agents and tasks
agent_defs = load_yaml("agents.yaml")
task_defs = load_yaml("tasks.yaml")

agents = {}
for a in agent_defs:
    agents[a['name']] = Agent(
        role=a['role'],
        goal=a['goal'],
        backstory=a['backstory'],
        verbose=a['verbose']
    )

tasks = []
for t in task_defs:
    agent = agents[t['agent']]
    tasks.append(Task(
    description=t['task'],
    expected_output=t['expected_output'],
    agent=agent
))

# Create and run the Crew
crew = Crew(agents=list(agents.values()), tasks=tasks, verbose=True)
crew.kickoff()
