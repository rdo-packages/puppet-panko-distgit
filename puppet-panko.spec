%{!?upstream_version: %global upstream_version %{version}%{?milestone}}

%define upstream_name openstack-panko

Name:                   puppet-panko
Version:                15.4.0
Release:                1%{?dist}
Summary:                Puppet module for OpenStack Panko Service
License:                ASL 2.0

URL:                    https://launchpad.net/puppet-panko

Source0:                https://tarballs.openstack.org/%{name}/%{name}-%{upstream_version}.tar.gz

BuildArch:              noarch

Requires:               puppet-inifile
Requires:               puppet-keystone
Requires:               puppet-stdlib
Requires:               puppet-openstacklib
Requires:               puppet-oslo
Requires:               puppet >= 2.7.0

%description
Installs and configures OpenStack Panko Events Service.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

find . -type f -name ".*" -exec rm {} +
find . -size 0 -exec rm {} +
find . \( -name "*.pl" -o -name "*.sh"  \) -exec chmod +x {} +
find . \( -name "*.pp" -o -name "*.py"  \) -exec chmod -x {} +
find . \( -name "*.rb" -o -name "*.erb" \) -exec chmod -x {} +
find . \( -name spec -o -name ext \) | xargs rm -rf

%build


%install
rm -rf %{buildroot}
install -d -m 0755 %{buildroot}/%{_datadir}/openstack-puppet/modules/panko/
cp -rp * %{buildroot}/%{_datadir}/openstack-puppet/modules/panko/



%files
%{_datadir}/openstack-puppet/modules/panko/


%changelog
* Fri Oct 04 2019 RDO <dev@lists.rdoproject.org> 15.4.0-1
- Update to 15.4.0



