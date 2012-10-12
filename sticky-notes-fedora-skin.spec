Name:       sticky-notes-fedora-skin
Version:    0.1
Release:    1%{?dist}
Summary:    A Fedora skin for Sticky notes

License:    GPLv2+
URL:        https://github.com/athmane/sticky-notes-fedora-skin	
Source0:    sticky-notes-fedora-skin-0.1.tar.gz	

Requires:   sticky-notes	
BuildArch:  noarch

%description
A Fedora skin for Sticky notes, a free and open source 
paste-bin application.

%prep
%setup -q


%build
# nothing to build

%install
# Remove exec perms on files
find . -type f -exec chmod -x {} \;

mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/sticky-notes/skins
cp -pr fedora ${RPM_BUILD_ROOT}%{_datadir}/sticky-notes/skins

%files
%doc README.*
%{_datadir}/sticky-notes/skins/fedora


%changelog
* Thu Jul 26 2012 Athmane Madjoudj <athmane@fedoraproject.org> 0.1-1
- First spec.


