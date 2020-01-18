%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%endif

%global tarball_name iso8601

Name:           python-iso8601
Version:        0.1.10
Release:        1%{?dist}
Summary:        Simple module to parse ISO 8601 dates

Group:          Development/Languages
License:        MIT
URL:            http://pypi.python.org/pypi/iso8601/
Source0:        http://pypi.python.org/packages/source/i/iso8601/%{tarball_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python2-devel python-setuptools

%description
This module parses the most common forms of ISO 8601 date strings (e.g.
2007-01-14T20:34:22+00:00) into datetime objects.


%prep
%setup -qn %{tarball_name}-%{version}


%build
%{__python} setup.py build


%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --skip-build --root %{buildroot}


%clean
rm -rf %{buildroot}


%files
%defattr(-,root,root,-)
%doc LICENSE README.rst
%{python_sitelib}/*


%changelog
* Thu Mar 27 2014 Pádraig Brady <pbrady@redhat.com> - 0.1.10-1
- Latest upstream

* Tue Nov 12 2013 Pádraig Brady <pbrady@redhat.com> - 0.1.8-1
- Latest upstream

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul  9 2010 Ian Weller <iweller@redhat.com> - 0.1.4-2
- Correct python_sitelib macro

* Mon Jun 28 2010 Ian Weller <iweller@redhat.com> - 0.1.4-1
- Initial package build
