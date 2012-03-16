%define api_version 2.4
%define realapi 1.4
%define major 1
%define libname %mklibname %{name} %{api_version} %{major}
%define libnamedev %mklibname -d %{name} %{api_version}
%define libnamestaticdev %mklibname -d -s %{name} %{api_version}
%define oldlibname %mklibname gtkmm %api_version
%define olddevelname %mklibname -d gtkmm %api_version
%define oldstaticname %mklibname -s -d gtkmm %api_version

Name:		pangomm
Summary:	C++ interface for the pango library
Version:	2.28.4
Release:	3
License:	LGPLv2+
Group:		System/Libraries
URL:		http://gtkmm.org/
Source:		http://ftp.gnome.org/pub/GNOME/sources/%{name}/%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(mm-common-util)
BuildRequires:	pkgconfig(glibmm-2.4)
BuildRequires:	pkgconfig(cairomm-1.0)
BuildRequires:	pkgconfig(pango)
BuildRequires:	pkgconfig(pangocairo)

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
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}%{api_version}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Conflicts:	%olddevelname < 2.13.5

%description	-n %{libnamedev}
This package contains the headers and development files that are needed,
when trying to develop or compile applications which need %{name}.

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
%setup -q

%build
%configure2_5x \
    --enable-static \
    --enable-shared \
    --disable-static
%make

# make check does nothing

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -name \*.la|xargs rm -f

%files -n %{libname}
%{_libdir}/libpangomm-%{realapi}.so.%{major}*

%files -n %{libnamedev}
%doc COPYING ChangeLog AUTHORS COPYING NEWS README
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%{_libdir}/pangomm-%{realapi}/

%files doc
%doc %{_datadir}/doc/pangomm-%{realapi}/
%doc %{_datadir}/devhelp/books/*
