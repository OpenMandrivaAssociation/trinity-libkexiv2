%bcond clang 1

# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif
%define pkg_rel 4

%define tde_pkg libkexiv2

%define tde_prefix /opt/trinity

%define libname %mklibname kexiv2
%define devname %mklibname kexiv2 -d

%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%define _debugsource_template %{nil}

%define tarball_name %{tde_pkg}-trinity

Name:		trinity-%{tde_pkg}
Epoch:		2
Version:	0.1.7
Release:	%{?tde_version:%{tde_version}_}5
Summary:	Qt like interface for the libexiv2 library (runtime) [Trinity]
Group:		System/Libraries
URL:		http://www.trinitydesktop.org/

License:	GPLv2+

Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/libraries/%{tarball_name}-%{tde_version}.tar.xz

BuildSystem:    cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DINCLUDE_INSTALL_DIR=%{tde_prefix}/include/tde
BuildOption:    -DWITH_ALL_OPTIONS=ON -DBUILD_ALL=ON -DBUILD_DOC=ON
BuildOption:    -DBUILD_TRANSLATIONS=ON
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}

BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	desktop-file-utils
BuildRequires:	trinity-tde-cmake >= %{tde_version}
BuildRequires:	gettext

%{!?with_clang:BuildRequires:	gcc-c++}

# EXIV2
BuildRequires:  pkgconfig(exiv2)

# IDN support
BuildRequires:	pkgconfig(libidn)

# OPENSSL support
BuildRequires:  pkgconfig(openssl)

BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)

%description
libkexif2 contains the library of libkexiv2.
Libkexif is a wrapper around Exiv2 library to manipulate pictures metadata.

##########

%package -n trinity-%{libname}-5
Summary:	Qt like interface for the libexiv2 library (runtime) [Trinity]
Group:		System/Libraries

%description -n trinity-%{libname}-5
libkexif2 contains the library of libkexiv2.
Libkexif is a wrapper around Exiv2 library to manipulate pictures metadata.

%files -n trinity-%{libname}-5
%defattr(-,root,root,-)
%{tde_prefix}/%{_lib}/libkexiv2.so.5
%{tde_prefix}/%{_lib}/libkexiv2.so.5.0.0

##########

%package -n trinity-%{devname}
Group:		Development/Libraries/Other
Summary:	Qt like interface for the libexiv2 library (development) [Trinity]
Requires:	trinity-%{libname}-5 = %{EVRD}

%description -n trinity-%{devname}
libkexif2-devel contains development files and documentation for libkexiv2
library.  The library documentation is available on kexiv2.h header file.
Libkexif is a wrapper around Exiv2 library to manipulate pictures metadata.

%files -n trinity-%{devname}
%defattr(-,root,root,-)
%{tde_prefix}/%{_lib}/libkexiv2.so
%{tde_prefix}/%{_lib}/libkexiv2.la
%{tde_prefix}/include/tde/libkexiv2/
%{tde_prefix}/%{_lib}/pkgconfig/libkexiv2.pc


%conf -p
unset QTDIR QTINC QTLIB
export PATH="%{tde_prefix}/bin:${PATH}"

