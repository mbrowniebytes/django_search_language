from django.shortcuts import render, HttpResponse
from django.template import Context, loader
import requests
import json
import datetime
import time
from dateutil import parser
from django.utils import timezone

def index(request):
    return HttpResponse('Hello World!')

def test(request):
    return HttpResponse('Test view!')

def language(request):
    
    if request.method == 'POST':
        language = request.POST.get('language')
    else:
        language = "Python"
        
    url = 'https://api.github.com/search/repositories?q='+language+'&sort=updated&order=desc'
    req = requests.get(url)
    jsonItems = []
    jsonResult = json.loads(req.content)

    # test content so do not have to access github api often
    # testContent = '{"items":[{"id": 46629356, "name": "Orchard-Scripting-Extensions-PHP", "full_name": "Lombiq/Orchard-Scripting-Extensions-PHP", "owner": {"login": "Lombiq", "id": 8158177, "avatar_url": "https://avatars2.githubusercontent.com/u/8158177?v=4", "gravatar_id": "", "url": "https://api.github.com/users/Lombiq", "html_url": "https://github.com/Lombiq", "followers_url": "https://api.github.com/users/Lombiq/followers", "following_url": "https://api.github.com/users/Lombiq/following{/other_user}", "gists_url": "https://api.github.com/users/Lombiq/gists{/gist_id}", "starred_url": "https://api.github.com/users/Lombiq/starred{/owner}{/repo}", "subscriptions_url": "https://api.github.com/users/Lombiq/subscriptions", "organizations_url": "https://api.github.com/users/Lombiq/orgs", "repos_url": "https://api.github.com/users/Lombiq/repos", "events_url": "https://api.github.com/users/Lombiq/events{/privacy}", "received_events_url": "https://api.github.com/users/Lombiq/received_events", "type": "Organization", "site_admin": false}, "private": false, "html_url": "https://github.com/Lombiq/Orchard-Scripting-Extensions-PHP", "description": "A child module for Orchard Scripting Extensions for running PHP code inside Orchard.", "fork": false, "url": "https://api.github.com/repos/Lombiq/Orchard-Scripting-Extensions-PHP", "forks_url": "https://api.github.com/repos/Lombiq/Orchard-Scripting-Extensions-PHP/forks", "keys_url": "https://api.github.com/repos/Lombiq/Orchard-Scripting-Extensions-PHP/keys{/key_id}", "collaborators_url": "https://api.github.com/repos/Lombiq/Orchard-Scripting-Extensions-PHP/collaborators{/collaborator}", "teams_url": "https://api.github.com/repos/Lombiq/Orchard-Scripting-Extensions-PHP/teams", "hooks_url": "https://api.github.com/repos/Lombiq/Orchard-Scripting-Extensions-PHP/hooks", "issue_events_url": "https://api.github.com/repos/Lombiq/Orchard-Scripting-Extensions-PHP/issues/events{/number}", "events_url": "https://api.github.com/repos/Lombiq/Orchard-Scripting-Extensions-PHP/events", "assignees_url": "https://api.github.com/repos/Lombiq/Orchard-Scripting-Extensions-PHP/assignees{/user}", "branches_url": "https://api.github.com/repos/Lombiq/Orchard-Scripting-Extensions-PHP/branches{/branch}", "tags_url": "https://api.github.com/repos/Lombiq/Orchard-Scripting-Extensions-PHP/tags", "blobs_url": "https://api.github.com/repos/Lombiq/Orchard-Scripting-Extensions-PHP/git/blobs{/sha}", "git_tags_url": "https://api.github.com/repos/Lombiq/Orchard-Scripting-Extensions-PHP/git/tags{/sha}", "git_refs_url": "https://api.github.com/repos/Lombiq/Orchard-Scripting-Extensions-PHP/git/refs{/sha}", "trees_url": "https://api.github.com/repos/Lombiq/Orchard-Scripting-Extensions-PHP/git/trees{/sha}", "statuses_url": "https://api.github.com/repos/Lombiq/Orchard-Scripting-Extensions-PHP/statuses/{sha}", "languages_url": "https://api.github.com/repos/Lombiq/Orchard-Scripting-Extensions-PHP/languages", "stargazers_url": "https://api.github.com/repos/Lombiq/Orchard-Scripting-Extensions-PHP/stargazers", "contributors_url": "https://api.github.com/repos/Lombiq/Orchard-Scripting-Extensions-PHP/contributors", "subscribers_url": "https://api.github.com/repos/Lombiq/Orchard-Scripting-Extensions-PHP/subscribers", "subscription_url": "https://api.github.com/repos/Lombiq/Orchard-Scripting-Extensions-PHP/subscription", "commits_url": "https://api.github.com/repos/Lombiq/Orchard-Scripting-Extensions-PHP/commits{/sha}", "git_commits_url": "https://api.github.com/repos/Lombiq/Orchard-Scripting-Extensions-PHP/git/commits{/sha}", "comments_url": "https://api.github.com/repos/Lombiq/Orchard-Scripting-Extensions-PHP/comments{/number}", "issue_comment_url": "https://api.github.com/repos/Lombiq/Orchard-Scripting-Extensions-PHP/issues/comments{/number}", "contents_url": "https://api.github.com/repos/Lombiq/Orchard-Scripting-Extensions-PHP/contents/{+path}", "compare_url": "https://api.github.com/repos/Lombiq/Orchard-Scripting-Extensions-PHP/compare/{base}...{head}", "merges_url": "https://api.github.com/repos/Lombiq/Orchard-Scripting-Extensions-PHP/merges", "archive_url": "https://api.github.com/repos/Lombiq/Orchard-Scripting-Extensions-PHP/{archive_format}{/ref}", "downloads_url": "https://api.github.com/repos/Lombiq/Orchard-Scripting-Extensions-PHP/downloads", "issues_url": "https://api.github.com/repos/Lombiq/Orchard-Scripting-Extensions-PHP/issues{/number}", "pulls_url": "https://api.github.com/repos/Lombiq/Orchard-Scripting-Extensions-PHP/pulls{/number}", "milestones_url": "https://api.github.com/repos/Lombiq/Orchard-Scripting-Extensions-PHP/milestones{/number}", "notifications_url": "https://api.github.com/repos/Lombiq/Orchard-Scripting-Extensions-PHP/notifications{?since,all,participating}", "labels_url": "https://api.github.com/repos/Lombiq/Orchard-Scripting-Extensions-PHP/labels{/name}", "releases_url": "https://api.github.com/repos/Lombiq/Orchard-Scripting-Extensions-PHP/releases{/id}", "deployments_url": "https://api.github.com/repos/Lombiq/Orchard-Scripting-Extensions-PHP/deployments", "created_at": "2015-11-21T19:06:41Z", "updated_at": "2017-07-11T18:01:16Z", "pushed_at": "2017-11-11T22:18:37Z", "git_url": "git://github.com/Lombiq/Orchard-Scripting-Extensions-PHP.git", "ssh_url": "git@github.com:Lombiq/Orchard-Scripting-Extensions-PHP.git", "clone_url": "https://github.com/Lombiq/Orchard-Scripting-Extensions-PHP.git", "svn_url": "https://github.com/Lombiq/Orchard-Scripting-Extensions-PHP", "homepage": null, "size": 1652, "stargazers_count": 0, "watchers_count": 0, "language": "C#", "has_issues": true, "has_projects": true, "has_downloads": true, "has_wiki": true, "has_pages": false, "forks_count": 0, "mirror_url": null, "archived": false, "open_issues_count": 0, "forks": 0, "open_issues": 0, "watchers": 0, "default_branch": "master", "score": 1.7344921}]}'
    # jsonResult = json.loads(testContent)
    jsonItems = jsonResult['items']

    parsedData = []
    for data in jsonItems:
        userData = {}
        userData['name'] = data['name']
        userData['html_url'] = data['html_url']
        userData['full_name'] = data['full_name']
        userData['description'] = data['description']
        userData['owner'] = {}
        userData['owner']['avatar_url'] = data['owner']['avatar_url']
        userData['stargazers_count'] = data['stargazers_count']
        userData['watchers_count'] = data['watchers_count']
        userData['forks_count'] = data['forks_count']
        dt = parser.parse(data['pushed_at'])
        dt = timezone.localtime(dt)        
        userData['pushed_at'] = dt.strftime("%I:%M:%S%p %Y-%m-%d")
        dt = parser.parse(data['created_at'])
        dt = timezone.localtime(dt)
        userData['created_at'] = dt.strftime("%I:%M:%S%p %Y-%m-%d")
        parsedData.append(userData)
    # return HttpResponse(parsedData)
    
    return render(request, 'app/language.html', {'data': parsedData, 'language': language})

