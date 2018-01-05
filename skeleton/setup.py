try:
	from setuptools import setup
except ImportError:
	from disutils.core import setup

config = {
	'description': 'project_name',
	'author': 'Michal Sznajder',
	'url': 'url where you find it',
	'download_url': 'url where you download it',
	'author_email': 'msznajder@gmail.com',
	'version': '0.1',
	'install_required': ['nose'],
	'packages': ['project_name'],
	'scripts': [],
	'name': 'project_name'
}

setup(**config)
