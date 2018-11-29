
from nose.tools import *
from saltscaffold import formulafolders, formulafiles
import os
import shutil

target_dir = os.path.normpath(os.path.join(os.getcwd(),"testcruft"))

def setup():
    os.mkdir(target_dir) # temp dir for holding tests
    print("root test directory: {dir}".format(dir=target_dir))

def teardown():
    print("attempting to tear down: {dir}".format(dir=target_dir))
    shutil.rmtree(target_dir)

def test_create_folder_path():
    sub_dir = "magicdir"
    expected_path = os.path.join(os.path.normpath(target_dir), sub_dir)
    resultant_path = formulafolders.create_path(target_dir, sub_dir)
    assert expected_path == resultant_path

def test_create_folders():
    formula_name = "waller"
    formulafolders.create_folders(formula_name, target_dir) # Create the formula folders
    assert_folder_exists(target_dir, formula_name) # testcruft/waller-formula exists
    assert_folder_exists(target_dir, formula_name + "/files") # testcruft/waller-formula/waller exists

def test_create_files():
    formula_name = "salzburg"
    formulafolders.create_folders(formula_name, target_dir) # Create the formula folders
    states_root = formulafolders.create_path(target_dir, formula_name)
    # write out all the files in the root directory
    formulafiles.write_file(formula_name, states_root, None, ".kitchen.yml", " +++")
    formulafiles.write_file(formula_name, states_root, None, ".kitchen.ci.yml", " +++")
    formulafiles.write_file(formula_name, states_root, None, "Jenkinsfile", " +++")
    formulafiles.write_file(formula_name, states_root, None, "pillar-custom.sls", " +++")
    formulafiles.write_file(formula_name, states_root, None, "defaults.yml", " +++")
    formulafiles.write_file(formula_name, states_root, None, "map.jinja", " +++")
    formulafiles.write_file(formula_name, states_root, None, "init.sls", " +++")
    formulafiles.write_file(formula_name, states_root, None, "install.sls", " +++")
    formulafiles.write_file(formula_name, states_root, None, "config.sls", " +++")
    formulafiles.write_file(formula_name, states_root, None, "service.sls", " +++")
    formulafiles.write_file(formula_name, states_root, "files","config.conf.jinja", " +++")
    formulafiles.write_file(formula_name, states_root, "test/default", "conftest.py", " +++")
    formulafiles.write_file(formula_name, states_root, "test/default", "test_pkg.py", " +++")
    formulafiles.write_file(formula_name, states_root, "test/default", "test_conf.py", " +++")
    formulafiles.write_file(formula_name, states_root, "test/default", "test_service.py", " +++")

    assert_file_exists(states_root, None, ".kitchen.yml")
    assert_file_exists(states_root, None, ".kitchen.ci.yml")
    assert_file_exists(states_root, None, "Jenkinsfile")
    assert_file_exists(states_root, None, "pillar-custom.sls")
    assert_file_exists(states_root, None, "defaults.yml")
    assert_file_exists(states_root, None, "map.jinja")
    assert_file_exists(states_root, None, "init.sls")
    assert_file_exists(states_root, None, "install.sls")
    assert_file_exists(states_root, None, "config.sls")
    assert_file_exists(states_root, None, "service.sls")
    assert_file_exists(states_root, "files", "config.conf.jinja")
    assert_file_exists(states_root, "test/default", "conftest.py")
    assert_file_exists(states_root, "test/default", "test_pkg.py")
    assert_file_exists(states_root, "test/default", "test_conf.py")
    assert_file_exists(states_root, "test/default", "test_service.py")

def assert_file_exists(target_dir, sub_dir, filename):
    """Tests if a file exists  or not"""
    if sub_dir == None:
        assert os.path.exists(os.path.join(target_dir, filename))
    else:
        assert os.path.exists(os.path.join(os.path.join(target_dir, sub_dir), filename))


def assert_folder_exists(target_dir, sub_dir):
    """Tests to see if a particular folder exists"""
    assert os.path.exists(os.path.join(target_dir, sub_dir))
