%if 0%{?rhel} == 6
%define cmake_pkg cmake28
%else
%define cmake_pkg cmake
%endif

Name:		qterminal
Version:	0.6.0
Release:	4%{?dist}
License:	GPLv2
URL:		https://github.com/qterminal/qterminal
Source0:	https://github.com/%{name}/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:	%{name}-qt5.desktop
Source2:	%{name}_drop-qt5.desktop
Summary:	Advanced terminal emulator
Requires:	qterminal-common
BuildRequires:	desktop-file-utils
BuildRequires:  %{cmake_pkg} >= 2.8
BuildRequires:	libqxt-devel
BuildRequires:	pkgconfig(QtGui)
# qtermwidget-devel
BuildRequires:	pkgconfig(qtermwidget4) >= 0.6.0

%description
Advanced terminal emulator with many useful bells and whistles.


%package	qt5
Summary:	Advanced terminal emulator (qt5)
Requires:	qterminal-common
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	qt5-qttools-devel
# qtermwidget-qt5-devel
BuildRequires:	pkgconfig(qtermwidget5) >= 0.6.0

%description	qt5
Advanced terminal emulator (qt5 version) with many useful bells and whistles.


%package	common
Summary:	Qterminal common files

%description	common
Common files for Qterminal as qt4 as qt5 versions.


%prep
%setup -q
#rm -rf src/third-party


%build
mkdir build4
pushd build4
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo ..
make %{?_smp_mflags}
popd
mkdir build5
pushd build5
cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo -DUSE_QT5=ON -DUSE_SYSTEM_QXT=OFF -DCMAKE_INSTALL_PREFIX=/usr ..
make %{?_smp_mflags}
popd


%install
pushd build5
%make_install
mv %{buildroot}%{_bindir}/%{name} %{buildroot}%{_bindir}/%{name}-qt5
install -m644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}-qt5.desktop
install -m644 %{SOURCE2} %{buildroot}%{_datadir}/applications/%{name}_drop-qt5.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}-qt5.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}_drop-qt5.desktop
popd
pushd build4
%make_install
popd
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}_drop.desktop
%find_lang %{name} --with-qt --without-mo


%files
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}_drop.desktop

%files	qt5
%{_bindir}/%{name}-qt5
%{_datadir}/applications/%{name}-qt5.desktop
%{_datadir}/applications/%{name}_drop-qt5.desktop

%files	common -f %{name}.lang
%license COPYING
%doc AUTHORS CONTRIBUTING.md README
%{_datadir}/pixmaps/%{name}.png


%changelog
* Wed Dec 2 2015 TI_Eugene <ti.eugene@gmail.com> - 0.6.0-4
- Qt5 version added

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Apr 10 2015 TI_Eugene <ti.eugene@gmail.com> - 0.6.0-2
- Rebuild with new qtermwidget

* Tue Nov 04 2014 TI_Eugene <ti.eugene@gmail.com> - 0.6.0-1
- Version bump

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Nov 19 2013 TI_Eugene <ti.eugene@gmail.com> - 0.4.0-5
- Next git snapshot
- Changelog dates (year) fixed

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 07 2013 TI_Eugene <ti.eugene@gmail.com> - 0.4.0-3
- Source URL update
- second desktop validate added

* Mon May 06 2013 TI_Eugene <ti.eugene@gmail.com> - 0.4.0-2
- Source URL update

* Mon May 06 2013 TI_Eugene <ti.eugene@gmail.com> - 0.4.0-1
- initial packaging for Fedora
