from cx_freeze import setup, Executable

setup(
	name="salut",
	version='0.1',
	description="C'est un programme de chiffrement",
	executable=[Executable('test.py')],

)