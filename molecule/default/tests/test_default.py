import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


dashboard_user = 'ubuntu'
dashboard_app_dir = '/var/www/dashboard/new'
php_major_minor_version = '7.3'


def test_app_dir(host):
    app_dir = host.file(dashboard_app_dir)

    assert app_dir.is_directory
    assert app_dir.user == dashboard_user
    assert app_dir.group == dashboard_user
    assert app_dir.mode == 0o755


def test_app_git_dir(host):
    git_dir = host.file('%s/.git' % dashboard_app_dir)

    assert git_dir.is_directory
    assert git_dir.user == dashboard_user
    assert git_dir.group == dashboard_user
    assert git_dir.mode == 0o755


def test_app_vendor_dir(host):
    """Test the composer dependencies were installed."""
    vendor_dir = host.file('%s/vendor' % dashboard_app_dir)

    assert vendor_dir.is_directory
    assert vendor_dir.user == dashboard_user
    assert vendor_dir.group == dashboard_user
    assert vendor_dir.mode == 0o755


def test_app_env(host):
    env = host.file('%s/.env' % dashboard_app_dir)

    assert env.exists
    assert env.user == dashboard_user
    assert env.group == 'www-data'
    assert env.mode == 0o640

    assert env.contains(
        "DB_PASSWORD='superpassword'"
    )

    assert env.contains(
        "PRE_APPROVED_ADMINS=''"
    )


def test_log_dir(host):
    log_dir = host.file('/var/log/dashboard')

    assert log_dir.exists
    assert log_dir.is_directory
    assert log_dir.user == dashboard_user
    assert log_dir.group == dashboard_user


def test_supervisor_conf(host):
    supervisor = host.file('/etc/supervisor/conf.d/dashboard.conf')

    assert supervisor.exists
    assert supervisor.user == 'root'
    assert supervisor.group == 'root'
    assert supervisor.mode == 0o644
    assert supervisor.contains('program:dashboard-campaign-status-download')
    assert supervisor.contains('program:dashboard-campaign-status-full-scan')
    assert supervisor.contains('user=%s' % dashboard_user)


def test_cron(host):
    cron = host.file('/etc/cron.d/dashboard')

    assert cron.exists
    assert cron.user == 'root'
    assert cron.group == 'root'
    assert cron.mode == 0o644
    assert cron.contains(
        'supervisorctl start dashboard-campaign-status-download')
    assert cron.contains(
        'supervisorctl start dashboard-campaign-status-full-scan')


def test_nginx(host):
    nginx = host.service('nginx')

    assert nginx.is_enabled
    assert nginx.is_running


def test_php_fpm(host):
    php_fpm = host.service('php%s-fpm' % php_major_minor_version)

    assert php_fpm.is_enabled
    assert php_fpm.is_running
