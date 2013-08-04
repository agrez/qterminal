%global commit b6a9de2f53f5ea535d17bbf5612e0fd618aebee1
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:		qterminal
Version:	0.4.0
Release:	4%{?dist}
License:	GPLv2
#Source0:	https://github.com/qterminal/qerminal/archive/%{commit}/%{name}-%{version}-%{shortcommit}.tar.gz
Source0:	https://github.com/qterminal/qterminal/tarball/%{commit}/%{name}-%{name}-%{version}-%{shortcommit}.tar.gz
Source1:	FindQxt.cmake
Patch0:		%{name}-%{version}-qxt.patch
Patch1:		%{name}-%{version}-fsf.patch
Summary:	Advanced terminal emulator
URL:		https://github.com/qterminal/qterminal
BuildRequires:	cmake, pkgconfig(QtGui), qtermwidget-devel, libqxt-devel, desktop-file-utils

%description
Advanced terminal emulator with many useful bells and whistles.

%prep
%setup -qn %{name}-%{name}-%{shortcommit}
%patch0 -p 0
%patch1 -p 0
cp %{SOURCE1} cmake/modules
rm -rf src/third-party

%build
mkdir build
pushd build
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo ..
make %{?_smp_mflags}
popd

%install
pushd build
%make_install
popd
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}_drop.desktop
%find_lang %{name} --with-qt --without-mo

%files -f %{name}.lang
%doc AUTHORS COPYING README
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 07 2012 TI_Eugene <ti.eugene@gmail.com> - 0.4.0-3
- Source URL update
- second desktop validate added

* Mon May 06 2012 TI_Eugene <ti.eugene@gmail.com> - 0.4.0-2
- Source URL update

* Mon May 06 2012 TI_Eugene <ti.eugene@gmail.com> - 0.4.0-1
- initial packaging for Fedora
