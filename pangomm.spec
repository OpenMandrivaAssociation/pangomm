%define version 2.28.0
%define release %mkrel 1

%define glibmm_version 2.14.1
%define pango_version 1.5.2
%define cairomm_version 1.2.2
%define name pangomm
%define api_version 2.4
%define realapi 1.4
%define major 1
%define libname %mklibname %{name} %{api_version} %{major}
%define libnamedev %mklibname -d %{name} %{api_version}
%define libnamestaticdev %mklibname -d -s %{name} %{api_version}
%define oldlibname %mklibname gtkmm %api_version
%define olddevelname %mklibname -d gtkmm %api_version
%define oldstaticname %mklibname -s -d gtkmm %api_version

Name:		%{name}
Summary:	C++ interface for the pango library
Version:	%{version}
Release:	%{release}
License:	LGPLv2+
Group:		System/Libraries
URL:		http://gtkmm.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source:		http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
BuildRequires:	glibmm2.4-devel >= %{glibmm_version}
BuildRequires:	libpango-devel >= %pango_version
BuildRequires:	cairomm-devel  >= %cairomm_version

%description
Pangomm provides a C++ interface to the Pango library. Highlights
include typesafe callbacks, widgets extensible via inheritance and a
comprehensive set of widget classes that can be freely combined to
quickly create complex user interfaces.


%package	-n %{libname}
Summary:	C++ interface for the pango library
Group:		System/Libraries
Provides:	%{name}%{api_version} = %{version}-%{release}
Conflicts:	%oldlibname < 2.13.5

%description	-n %{libname}
Gtkmm provides a C++ interface to the GTK+ GUI library. Gtkmm2 wraps GTK+ 2.
Highlights include typesafe callbacks, widgets extensible via inheritance
and a comprehensive set of widget classes that can be freely combined to
quickly create complex user interfaces.

This package contains the library needed to run programs dynamically
linked with %{name}.


%package	-n %{libnamedev}
Summary:	Headers and development files of %{name}
Group:		Development/GNOME and GTK+
Requires:	%{libname} = %{version}
Provides:	%{name}%{api_version}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Requires:	glibmm2.4-devel >= %{glibmm_version}
Conflicts:	%olddevelname < 2.13.5

%description	-n %{libnamedev}
This package contains the headers and development files that are needed,
when trying to develop or compile applications which need %{name}.


%package	-n %{libnamestaticdev}
Summary:	Static libraries of %{name}
Group:		Development/GNOME and GTK+
Requires:	%{libnamedev} = %{version}
Provides:	%{name}-static-devel = %{version}-%{release}
Conflicts:	%oldstaticname < 2.13.5

%description	-n %{libnamestaticdev}
This package contains the static libraries of %{name}.


%package	doc
Summary:	GTKmm documentation
Group:		Books/Other

%description	doc
Pangomm provides a C++ interface to the Pango library. Highlights
include typesafe callbacks, widgets extensible via inheritance and a
comprehensive set of widget classes that can be freely combined to
quickly create complex user interfaces.

This package contains all API documentation for pangomm. You can readily read
this documentation with devhelp, a documentation reader.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x --enable-static --enable-shared
%make

# make check does nothing

%install
rm -rf %{buildroot}
%makeinstall_std

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-, root, root)
%doc AUTHORS COPYING NEWS README
%{_libdir}/libpangomm-%{realapi}.so.%{major}*


%files -n %{libnamedev}
%defattr(-, root, root)
%doc COPYING ChangeLog
%{_includedir}/*
%{_libdir}/*.la
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%_libdir/pangomm-%realapi

%files -n %{libnamestaticdev}
%defattr(-, root, root)
%doc COPYING
%{_libdir}/*.a

%files doc
%defattr(-, root, root)
%doc %{_datadir}/doc/pangomm-%realapi
%doc %{_datadir}/devhelp/books/*


