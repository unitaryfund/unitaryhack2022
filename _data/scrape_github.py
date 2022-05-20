# -*- coding: utf-8 -*-
from github import Github
import json
import os
from datetime import datetime
import frontmatter
from urllib import parse

# using an access token
g = Github(os.getenv('GITHUB_TOKEN'))

project_path = "../projects"
projects = {}
tags = ["[unitaryHACK]", "[unitaryhack]", "[UnitaryHACK]", "[UnitaryHack]"]

def pr_info(pr):
    keys = ['number', 'state', 'title', 'user', 'merged', 'merged_by', 'created_at', 'merged_at', 'closed_at']
    info = {key : getattr(pr, key) for key in keys if key in pr}
    return {key : i.strftime('%d/%m/%Y %H:%M:%S') if type(i)==datetime.datetime else i for key, i in info.items()} 



# Scrape the md project files for the yaml metadata
for filename in os.listdir(project_path):
    if filename.endswith(".md"):
        print(os.path.join(project_path,filename))
        p = frontmatter.load(os.path.join(project_path,filename))
        projects[p["title"]] = p.metadata
        projects[p["title"]]["full_title"] = (parse.urlparse(p["project_url"]).path).strip("/")
        projects[p["title"]]["date"] = (projects[p["title"]]["date"]).strftime('%d/%m/%Y %H:%M:%S')

# Results for a project should look like this:
#
# projects["mitiq"] = 
# {'title': 'Mitiq',
#  'emoji': '�🌴',
#  'project_url': 'https://github.com/unitaryfund/mitiq',
#  'full_name': 'unitaryfund/mitiq',
#  'metaDescription': 'Making NISQ hardware less noisy with a Python-based error mitigating package.',
#  'date': datetime.datetime(2019, 1, 1, 0, 0, tzinfo=datetime.timezone.utc),
#  'summary': 'Python package for quantum error mitigation techniques',
#  'tags': ['error-mitigation', 'noise', 'run-on-hardware', 'python'],
#  'bounties': [{'name': 'Redundant information in citation file',
#    'issue_num': 1227,
#    'value': 50},
#   {'name': 'Use consistent citation style in docs and function doctrings.',
#    'issue_num': 1250,
#    'value': 75},
#   {'name': 'Include backend in execute_with_shots',
#    'issue_num': 1163,
#    'value': 75},
#   {'name': 'Improve H2 example', 'issue_num': 1094, 'value': 100}],
#  'full_title': 'unitaryfund/mitiq'}

# Call GH api to get all repos that are part of the unitaryHACK event and bounty issues
for project, meta in projects.items():
    # Get the GH data for the repo
    project_data = g.get_repo(meta["full_title"])
    # Add the GH data to the projects dict
    meta.update(project_data.__dict__["_rawData"])
    # Get the PRs for the repo
    prs = project_data.get_pulls(sort='created')
    # Add the PRs with the hackathon tag to the projects dict
    meta["uh_prs"] = [pr_info(pr) for pr in prs if any(x in pr.title for x in tags)]
    # Look up the bountied issues and check on status
    if "bounties" in meta:
        for bounty in meta["bounties"]:
            issue_data = project_data.get_issue(bounty["issue_num"])
            bounty.update(issue_data.__dict__["_rawData"])

with open("gh.json", "w") as f:
    json.dump(projects, f)

print("Done! ♥")


# Results for the data on an issue should look like this:
#
# issue_data.__dict__["_rawData"] = 
# {'url': 'https://api.github.com/repos/unitaryfund/mitiq/issues/1094',
#  'repository_url': 'https://api.github.com/repos/unitaryfund/mitiq',
#  'labels_url': 'https://api.github.com/repos/unitaryfund/mitiq/issues/1094/labels{/name}',
#  'comments_url': 'https://api.github.com/repos/unitaryfund/mitiq/issues/1094/comments',
#  'events_url': 'https://api.github.com/repos/unitaryfund/mitiq/issues/1094/events',
#  'html_url': 'https://github.com/unitaryfund/mitiq/issues/1094',
#  'id': 1107045969,
#  'node_id': 'I_kwDODhvcQc5B_C5R',
#  'number': 1094,
#  'title': '[unitaryhack-bounty] Improve H2 example',
#  'user': {'login': 'andreamari',
#   'id': 46054446,
#   'node_id': 'MDQ6VXNlcjQ2MDU0NDQ2',
#   'avatar_url': 'https://avatars.githubusercontent.com/u/46054446?v=4',
#   'gravatar_id': '',
#   'url': 'https://api.github.com/users/andreamari',
#   'html_url': 'https://github.com/andreamari',
#   'followers_url': 'https://api.github.com/users/andreamari/followers',
#   'following_url': 'https://api.github.com/users/andreamari/following{/other_user}',
#   'gists_url': 'https://api.github.com/users/andreamari/gists{/gist_id}',
#   'starred_url': 'https://api.github.com/users/andreamari/starred{/owner}{/repo}',
#   'subscriptions_url': 'https://api.github.com/users/andreamari/subscriptions',
#   'organizations_url': 'https://api.github.com/users/andreamari/orgs',
#   'repos_url': 'https://api.github.com/users/andreamari/repos',
#   'events_url': 'https://api.github.com/users/andreamari/events{/privacy}',
#   'received_events_url': 'https://api.github.com/users/andreamari/received_events',
#   'type': 'User',
#   'site_admin': False},
#  'labels': [{'id': 1812908008,
#    'node_id': 'MDU6TGFiZWwxODEyOTA4MDA4',
#    'url': 'https://api.github.com/repos/unitaryfund/mitiq/labels/documentation',
#    'name': 'documentation',
#    'color': '0075ca',
#    'default': True,
#    'description': 'Improvements or additions to documentation'},
#   {'id': 1812908014,
#    'node_id': 'MDU6TGFiZWwxODEyOTA4MDE0',
#    'url': 'https://api.github.com/repos/unitaryfund/mitiq/labels/good%20first%20issue',
#    'name': 'good first issue',
#    'color': '7057ff',
#    'default': True,
#    'description': 'Good for newcomers'},
#   {'id': 3067329697,
#    'node_id': 'MDU6TGFiZWwzMDY3MzI5Njk3',
#    'url': 'https://api.github.com/repos/unitaryfund/mitiq/labels/priority/p2',
#    'name': 'priority/p2',
#    'color': 'D19B10',
#    'default': False,
#    'description': 'A non-urgent issue to fix or idea to discuss.'},
#   {'id': 3951006758,
#    'node_id': 'LA_kwDODhvcQc7rf5Qm',
#    'url': 'https://api.github.com/repos/unitaryfund/mitiq/labels/unitaryhack-bounty',
#    'name': 'unitaryhack-bounty',
#    'color': '0E8A16',
#    'default': False,
#    'description': ''},
#   {'id': 4105475738,
#    'node_id': 'LA_kwDODhvcQc70tJaa',
#    'url': 'https://api.github.com/repos/unitaryfund/mitiq/labels/self-contained-project',
#    'name': 'self-contained-project',
#    'color': 'F3888A',
#    'default': False,
#    'description': ''}],
#  'state': 'open',
#  'locked': False,
#  'assignee': None,
#  'assignees': [],
#  'milestone': None,
#  'comments': 2,
#  'created_at': '2022-01-18T15:30:12Z',
#  'updated_at': '2022-05-19T16:12:24Z',
#  'closed_at': None,
#  'author_association': 'MEMBER',
#  'active_lock_reason': None,
#  'body': "The current H2 example could be improved in two different aspects:\r\n\r\n- [ ] The numerical values of the Hamiltonian coefficients _g_j(R)_ are hard-coded from data extracted from a paper. It would be nice to derive them using some chemistry package e.g.: [PySCF](https://pyscf.org/) or [OpenFermion](https://github.com/quantumlib/OpenFermion). Ideally (but only 
# if not too complicated), it would be better to use the same Hamiltonian in order to reproduce the same results of the Mitiq paper. \r\n- [ ] Use a `mitiq.Observable` for the Hamiltonian, and just use `mitiq_cirq.compute_density_matrix` for the executor. See the docs for more details on how to define and use observables.\r\n\r\nIf you only fixed one of the two aspects, please don't close this issue but just mark the corresponding item in the above list.",
#  'closed_by': None,
#  'reactions': {'url': 'https://api.github.com/repos/unitaryfund/mitiq/issues/1094/reactions',
#   'total_count': 0,
#   '+1': 0,
#   '-1': 0,
#   'laugh': 0,
#   'hooray': 0,
#   'confused': 0,
#   'heart': 0,
#   'rocket': 0,
#   'eyes': 0},
#  'timeline_url': 'https://api.github.com/repos/unitaryfund/mitiq/issues/1094/timeline',
#  'performed_via_github_app': None,
#  'state_reason': None}