Summary:	Port of the MDA VST plugins to LV2
Summary(pl.UTF-8):	Port wtyczek VST MDA do LV2
Name:		lv2-mda-plugins
Version:	1.2.10
Release:	1
License:	GPL v3+
Group:		Libraries
Source0:	http://download.drobilla.net/mda-lv2-%{version}.tar.xz
# Source0-md5:	be5927457805943fc377bd56faae6373
URL:		http://drobilla.net/software/mda-lv2/
BuildRequires:	libstdc++-devel >= 6:4.7
BuildRequires:	lv2-devel >= 1.16.0
BuildRequires:	meson >= 0.56.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	lv2 >= 1.16.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoprovfiles	%{_libdir}/lv2

%description
This is a port of the MDA VST plugins to LV2.

%description -l pl.UTF-8
Ten pakiet zawiera port wtyczek VST MDA do LV2.

%prep
%setup -q -n mda-lv2-%{version}

%build
%meson

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NEWS README.md
%dir %{_libdir}/lv2/mda.lv2
%{_libdir}/lv2/mda.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/mda.lv2/*.so
