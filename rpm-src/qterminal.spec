Name:           qterminal
Version:        0.8.0
Release:        %mkrel 1
Summary:        QT-based multitab terminal emulator
License:        GPLv2
Group:          Terminals
URL:            https://github.com/lxde/qterminal
Source0:        https://github.com/lxde/%{name}/archive/%{version}.tar.gz/#/%{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Help)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5X11Extras)
BuildRequires:  pkgconfig(qtermwidget5)

BuildRequires:  cmake(lxqt)
BuildRequires:  cmake(lxqt-build-tools)

Requires:       lxqt-l10n

%description
QT-based multitab terminal emulator.
Based on QTermWidget by e_k@users.sourceforge.net

%prep
%setup -q

%build
%cmake_qt5 \
    -DPULL_TRANSLATIONS=NO

%make_build

%install
%make_install -C build

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}_drop.desktop

%files
%doc AUTHORS 
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}_drop.desktop
%{_iconsdir}/hicolor/*/*/%{name}.png
%{_datadir}/appdata/%{name}.appdata.xml


%changelog
* Tue May 01 2018 neoclust <neoclust> 0.8.0-1.mga6
  (not released yet)
+ Revision: 1224226
- New  version 0.8.0

* Wed Jan 18 2017 daviddavid <daviddavid> 0.7.1-1.mga6
+ Revision: 1082327
- new version: 0.7.1
- add BR lxqt-build-tools

* Fri Nov 11 2016 neoclust <neoclust> 0.7.0-2.mga6
+ Revision: 1066417
- Add translation package as a require

* Thu Nov 10 2016 neoclust <neoclust> 0.7.0-1.mga6
+ Revision: 1066200
- New version 0.7.0

* Sat Mar 05 2016 blino <blino> 0.6.0-2.mga6
+ Revision: 985967
- rebuild for armv5tl (also missed in first Mga6 mass rebuild)

* Sat Jan 09 2016 dglent <dglent> 0.6.0-1.mga6
+ Revision: 920701
- Version 0.6.0
- Qt5 build

* Wed Oct 15 2014 umeabot <umeabot> 0.4.0-6.mga5
+ Revision: 739242
- Second Mageia 5 Mass Rebuild

* Tue Sep 16 2014 umeabot <umeabot> 0.4.0-5.mga5
+ Revision: 688542
- Mageia 5 Mass Rebuild

* Sat Oct 19 2013 umeabot <umeabot> 0.4.0-4.mga4
+ Revision: 522687
- Mageia 4 Mass Rebuild

* Mon Mar 25 2013 matteo <matteo> 0.4.0-3.mga3
+ Revision: 405211
- added italian translations

* Sun Jan 13 2013 umeabot <umeabot> 0.4.0-2.mga3
+ Revision: 379980
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild

* Sun Jul 08 2012 matteo <matteo> 0.4.0-1.mga3
+ Revision: 268780
- spec file reviewed
- new version

* Thu Jan 05 2012 matteo <matteo> 0.2.0-3.mga2
+ Revision: 191931
- fixed license;spec file reviewed

* Mon Dec 19 2011 matteo <matteo> 0.2.0-2.mga2
+ Revision: 184344
- spec file reviewed

* Sun Dec 18 2011 matteo <matteo> 0.2.0-1.mga2
+ Revision: 183488
- fixed summary error
- fixed version number
- spec file cleaned
- imported package qterminal

