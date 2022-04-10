try:
	import requests as req, json, os, time
except ImportError as e:
	print('error',e)


def getdata():
	try:
		banner = """
		
		
 ______   __    __       ______              __     
/      \ |  \  |  \     /      \            |  \    
|  $$$$$$\ \$$ _| $$_   |  $$$$$$\  ______  _| $$_   
| $$ __\$$|  \|   $$ \  | $$ __\$$ /      \|   $$ \  
| $$|    \| $$ \$$$$$$  | $$|    \|  $$$$$$\\$$$$$$  
| $$ \$$$$| $$  | $$ __ | $$ \$$$$| $$    $$ | $$ __ 
| $$__| $$| $$  | $$|  \| $$__| $$| $$$$$$$$ | $$|  \

\$$    $$| $$   \$$  $$ \$$    $$ \$$     \  \$$  $$
 \$$$$$$  \$$    \$$$$   \$$$$$$   \$$$$$$$   \$$$$ 
		
[!] GitGet Tools For Get Information Users From API Github!
		"""
		
		os.system('clear')
		print(banner)
		ea = True
		while ea:
			username = str(input("Username Github : "))
			if (len(username) <= 2):
				os.system('clear')
				print("Please Input Correct Username!!")
				time.sleep(3)
				getdata()
			else:
				get = req.get(f"https://api.github.com/users/{username}").json()
				if ('"message": "Not Found"' in get):
					pass
				else:
					try:
						login = get['login']
						id = get['id']
						node_id = get['node_id']
						avatar_url = get['avatar_url']
						gravatar_id = get['gravatar_id']
						url = get['url']
						html_url = get['html_url']
						followers_url = get['followers_url']
						following_url = get['following_url']
						gists_url = get['gists_url']
						starred_url = get['starred_url']
						subscriptions_url = get['subscriptions_url']
						organizations_url = get['organizations_url']
						repos_url = get['repos_url']
						events_url = get['events_url']
						received_events_url = get['received_events_url']
						type = get['type']
						site_admin = get['site_admin']
						name = get['name']
						company = get['name']
						blog = get['blog']
						location = get['location']
						email = get['email']
						hireable = get['hireable']
						bio = get['bio']
						twitter_username = get['twitter_username']
						public_repos = get['public_repos']
						public_gists = get['public_gists']
						followers = get['followers']
						following = get['following']
						created_at = get['created_at']
						updated_at = get['updated_at']
					except:
			
						print('(!) IF ALL RESULT NULL, MAYBE USERNAME NOTFOUND!')
			
						login = 'null'
						id = 'null'
						node_id = 'null'
						avatar_url = 'null'
						gravatar_id = 'null'
						url = 'null'
						html_url = 'null'
						followers_url = 'null'			
						following_url = 'null'
						gists_url = 'null'
						starred_url = 'null'
						subscriptions_url = 'null'
						organizations_url = 'null'
						repos_url = 'null'
						events_url = 'null'
						received_events_url = 'null'
						type = 'null'
						site_admin = 'null'
						name = 'null'
						company = 'null'
						blog = 'null'
						location = 'null'
						email = 'null'
						hireable = 'null'
						bio = 'null'
						twitter_username = 'null'
						public_repos = 'null'
						public_gists = 'null'
						followers = 'null'
						following = 'null'
						created_at = 'null'
						updated_at = 'null'
				
				
			print(f"""
=======================================RESULT=======================================
login : {login}
id : {id}
node_id : {node_id}
avatar_url : {avatar_url}
gravatar_id : {gravatar_id}
url : {url}
html_url : {html_url}
followers_url : {followers_url}
following_url : {following_url}
gists_url : {gists_url}
starred_url : {starred_url}
subscriptions_url : {subscriptions_url}
organizations_url : {organizations_url}
repos_url : {repos_url}
events_url : {events_url}
received_events_url : {received_events_url}
type : {type}
site_admin : {site_admin}
name : {name}
company : {company}
blog : {blog}
location : {location}
email : {email}
hireable : {hireable}
bio : {bio}
twitter_username : {twitter_username}
public_repos : {public_repos}
public_gists : {public_gists}
followers : {followers}
following : {following}
created_at : {created_at}
updated_at : {updated_at}
=======================================END RESULT=======================================
			""")
	except Exception as b:
		print('error',b)
		
getdata()
