import os
from invoke import task, run

docs_dir = 'docs'
build_dir = os.path.join(docs_dir, '_build')

@task
def test():
    run("python run_tests.py", pty=True)

@task
def deps():
    print("Vendorizing nltk...")
    run("rm -rf text/nltk")
    run("git clone https://github.com/nltk/nltk.git")
    run("mv nltk/nltk text/")
    run("rm -rf nltk")

@task
def clean_docs():
    run("rm -rf %s" % build_dir)

@task
def browse_docs():
    run("open %s" % os.path.join(build_dir, 'index.html'))

@task
def build_docs(clean=False, browse=False):
    if clean:
        clean_docs()
    run("sphinx-build %s %s" % (docs_dir, build_dir), pty=True)
    if browse:
        browse_docs()