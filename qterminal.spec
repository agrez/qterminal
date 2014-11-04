%if 0%{?rhel} == 6
%define cmake_pkg cmake28
%else
%define cmake_pkg cmake
%endif

Name:		qterminal
Version:	0.6.0
Release:	1%{?dist}
License:	GPLv2
URL:		https://github.com/qterminal/qterminal
Source0:	https://github.com/%{name}/%{name}/releases/download/%{version}/%{name}-%{version}.tar.xz
Summary:	Advanced terminal emulator
BuildRequires:	desktop-file-utils
BuildRequires:  %{cmake_pkg} >= 2.8
BuildRequires:	pkgconfig(QtGui)
BuildRequires:	libqxt-devel
# qtermwidget-devel
BuildRequires:	pkgconfig(qtermwidget4) >= 0.6.0

%description
Advanced terminal emulator with many useful bells and whistles.


%prep
%setup -q
rm -rf src/third-party


%build
mkdir build
pushd build
%cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo ..
#cmake -DCMAKE_BUILD_TYPE=RelWithDebInfo -DUSE_QT5=ON ..
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
%doc AUTHORS CONTRIBUTING.md COPYING README
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/%{name}.png


%changelog
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
