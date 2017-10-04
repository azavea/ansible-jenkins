# ansible-jenkins

An Ansible role for installing Jenkins.

## Role Variables

- `jenkins_version` - Jenkins version (default: `2.*`).
- `jenkins_name` - Name of Jenkins user, corresponds to `$NAME` in `/etc/default/jenkins`. (default: `jenkins`)
- `jenkins_java_opts` - Java VM options for Jenkins. (defaults: `[-Djava.awt.headless=true, -Djava.net.preferIPv4Stack=true]`) See the Options section of the [Java man page](http://docs.oracle.com/javase/8/docs/technotes/tools/unix/java.html#BABDJJFI) for more information and choices.
- `jenkins_java_location` - Location of Jenkins binary. (default:  `/usr/bin/java`)
- `jenkins_pidfile_path` - Location of Jenkins pid file.  (default: `/var/run/$NAME/$NAME.pid`)
- `jenkins_war_path` -  Location of Jenkins WAR file. (default `/usr/share/$NAME/$NAME.war`)
- `jenkins_home_path` -  Main build and archive location for jenkins. (default: `/var/lib/$NAME`)
- `jenkins_run_standalone` - Run Jenkins in standalone mode. (default: `true`)
- `jenkins_log` -  Path to Jenkins logfile. (default: `/var/log/$NAME/$NAME.log`)
- `jenkins_umask` -  Use with the `jenkins_set_umask` to modify Jenkins default file permissions. (default: `022`)
- `jenkins_args` - List of arguments to pass to the Jenkins daemon. (defaults: `[--webroot=/var/cache/$NAME/war, --httpPort=$HTTP_PORT]`) See [Starting and Accessing Jenkins](https://wiki.jenkins-ci.org/display/JENKINS/Starting+and+Accessing+Jenkins) for a full set of arguments. 
- `jenkins_http_port` - Port on which Jenkins will run. (default: `8080`)

## Testing
Tests are done using [molecule](http://molecule.readthedocs.io/). To run the test suite, install molecule and its dependencies and run ` molecule test` from the folder containing molecule.yml. To add additional tests, add a [testinfra](http://testinfra.readthedocs.org/) python script in the [tests](./tests/) directory, or add a function to [test_jenkins.py](./tests/test_jenkins.py). Information about available Testinfra modules is available [here](http://testinfra.readthedocs.io/en/latest/modules.html).

### Example 
```
# Download molecule, dependencies
$ pip install molecule==1.25 ansible==2.4.*

# Change to the top-level project directory, which contains molecule.yml
$ cd /path/to/ansible-jenkins

# Ensure that molecule.yml is present
$ ls
CHANGELOG.md                             molecule.yml
LICENSE                                  playbook.retry
README.md                                playbook.yml
ansible.cfg                              tasks
defaults                                 templates
handlers                                 tests
meta                                     

# We're in the right directory, so let's run tests!
$ molecule test

```
