Summary:	Etrophy - library to manage scores, trophies and unlockables
Summary(pl.UTF-8):	Etrophy - biblioteka do zarządzania wynikami, trofeami i otwarciami
Name:		etrophy
Version:	0.5.1
Release:	3
License:	BSD
Group:		Libraries
Source0:	http://download.enlightenment.org/releases/%{name}-%{version}.tar.bz2
# Source0-md5:	ed8aabe52b71e54db6f9104725e61645
URL:		http://enlightenment.org/
BuildRequires:	ecore-devel >= 1.7.0
BuildRequires:	ecore-file-devel >= 1.7.0
BuildRequires:	edje
BuildRequires:	eet-devel >= 1.7.0
BuildRequires:	eina-devel >= 1.7.0
BuildRequires:	elementary-devel >= 1.7.0
BuildRequires:	evas-devel >= 1.7.0
BuildRequires:	pkgconfig >= 1:0.22
BuildRequires:	python >= 1:2.5
Requires:	ecore >= 1.7.0
Requires:	ecore-file >= 1.7.0
Requires:	eet >= 1.7.0
Requires:	eina >= 1.7.0
Requires:	elementary-libs >= 1.7.0
Requires:	evas >= 1.7.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Etrophy is a library that manages scores, trophies and unlockables. It
will store them and provide views to display them. Could be used by
games based on EFL.

%description -l pl.UTF-8
Etrophy to biblioteka zarządzająca wynikami, trofeami i otwarciami.
Może je przechowywać i udostępniać widoki do wyświetlania. Jest
przeznaczona przede wszystkim dla gier opartych na EFL.

%package devel
Summary:	Header files for Etrophy library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki Etrophy
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	ecore-devel >= 1.7.0
Requires:	ecore-file-devel >= 1.7.0
Requires:	eet-devel >= 1.7.0
Requires:	eina-devel >= 1.7.0
Requires:	elementary-devel >= 1.7.0
Requires:	evas-devel >= 1.7.0

%description devel
Header files for Etrophy library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki Etrophy.

%package static
Summary:	Static Etrophy library
Summary(pl.UTF-8):	Statyczna biblioteka Etrophy
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Etrophy library.

%description static -l pl.UTF-8
Statyczna biblioteka Etrophy.

%prep
%setup -q

%build
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libetrophy.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libetrophy.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libetrophy.so.0
%{_datadir}/etrophy

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libetrophy.so
%{_includedir}/etrophy-0
%{_pkgconfigdir}/etrophy.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libetrophy.a
