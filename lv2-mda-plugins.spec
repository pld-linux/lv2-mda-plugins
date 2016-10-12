Summary:	Port of the MDA VST plugins to LV2
Summary(pl.UTF-8):	Port wtyczek VST MDA do LV2
Name:		lv2-mda-plugins
Version:	1.2.2
Release:	2
License:	GPL v3+
Group:		Libraries
Source0:	http://download.drobilla.net/mda-lv2-%{version}.tar.bz2
# Source0-md5:	1962f48c54eafe52a3d2471cd3072aa8
URL:		http://drobilla.net/software/mda-lv2/
BuildRequires:	libstdc++-devel
BuildRequires:	lv2-devel >= 1.2.0
BuildRequires:	pkgconfig
BuildRequires:	python
Requires:	lv2 >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoprovfiles	%{_libdir}/lv2

%description
This is a port of the MDA VST plugins to LV2.

%description -l pl.UTF-8
Ten pakiet zawiera port wtyczek VST MDA do LV2.

%prep
%setup -q -n mda-lv2-%{version}

%build
CC="%{__cc}" \
CXX="%{__cxx}" \
CFLAGS="%{rpmcflags}" \
CXXFLAGS="%{rpmcxxflags}" \
LDFLAGS="%{rpmldflags}" \
./waf configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--strict

./waf -v

%install
rm -rf $RPM_BUILD_ROOT

./waf install \
	--destdir=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%dir %{_libdir}/lv2/mda.lv2
%{_libdir}/lv2/mda.lv2/*.ttl
%attr(755,root,root) %{_libdir}/lv2/mda.lv2/*.so
