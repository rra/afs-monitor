Name:           nagios-plugins-afs
Version:        2.4
Release:        1%{?dist}
Summary:        Nagios plugins for monitoring various aspects of AFS servers

Group:          Applications/System
License:        GPL+ or Artistic
URL:            http://www.eyrie.org/~eagle/software/afs-monitor
Source0:        http://archives.eyrie.org/software/afs/afs-monitor-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:       nagios-common,openafs,perl(Number::Format)

%description
afs-monitor provides Nagios-compatible probe scripts that can be used to
monitor AFS servers.  It contains five scripts: check_afs_quotas, which
monitors AFS volumes for quota usage; check_afs_space, which monitors
file server partitions for disk usage; check_afs_bos, which monitors any
bosserver-managed set of processes for problems reported by bos;
check_afs_rxdebug, which monitors AFS fileservers for connections
waiting for a thread; and check_afs_udebug, which monitors Ubik services
(such as vlserver and ptserver) for replication and quorum problems.

This package installs the plugins in %{_libdir}/nagios/plugins, for
compatibility with the nagios packages in Fedora/EPEL.

%prep
%setup -q -n afs-monitor-%{version}

%build
%define plugin_list bos quotas rxdebug space udebug
%define man_section 1

for plugin in %{plugin_list}; do
 pod2man --section=%{man_section} --center="Manual for %{name}" --release=%{version} \
  check_afs_$plugin check_afs_$plugin.%{man_section}
done

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_libdir}/nagios/plugins
for plugin in %{plugin_list}; do
 install -pm 755 check_afs_$plugin $RPM_BUILD_ROOT%{_libdir}/nagios/plugins
done

install -d $RPM_BUILD_ROOT%{_mandir}/man%{man_section}
for plugin in %{plugin_list}; do
 install -pm 644 check_afs_$plugin.%{man_section} $RPM_BUILD_ROOT%{_mandir}/man%{man_section}
done

install -d $RPM_BUILD_ROOT%{_defaultdocdir}/%name-%version
install -pm 644 README NEWS TODO $RPM_BUILD_ROOT%{_defaultdocdir}/%name-%version

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_libdir}/nagios/plugins/check_afs_*
%{_mandir}/man%{man_section}/check_afs_*
%doc %{_defaultdocdir}/%name-%version

%changelog
* Wed Jan 30 2013 Jacob Welsh <jwelsh@sinenomine.net> - 2.4-1
- Initial package
