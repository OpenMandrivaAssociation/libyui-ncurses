%define major 8
%define libname %mklibname yui %{major}-ncurses
%define develname %mklibname yui-ncurses -d

Name:		libyui-ncurses
Version:	2.43.9
Release:	1
Summary:	UI abstraction library - Ncurses plugin
License:	LGPLv2+
Group:		System/Libraries
Url:		https://github.com/libyui/libyui-ncurses
Source0:	https://github.com/libyui/libyui-ncurses/archive/master.tar.gz
Patch0:		libyui-ncurses-compile-workaround.patch

BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libyui) >= 3.1.2
BuildRequires:	pkgconfig(ncursesw)
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	qmake5
BuildRequires:	boost-devel
BuildRequires:	doxygen
BuildRequires:	texlive
BuildRequires:	graphviz
BuildRequires:	ghostscript
BuildRequires:	pkgconfig(fontconfig)
Requires:	libyui

%description
%{summary}.

%files
%{_bindir}/libyui-terminal

#-----------------------------------------------------------------------

%package -n %{libname}
Summary:	%{summary}
Group:		System/Libraries
Requires:	libyui
Requires:	%{_lib}qt5x11extras5
Provides:	%{name} = %{EVRD}
Provides:	libyui%{major}-qt = %{EVRD}

%description -n %{libname}
This package contains the library needed to run programs
dynamically linked with libyui-qt.

%files -n %{libname}
%{_libdir}/yui/lib*.so.*


#-----------------------------------------------------------------------

%package -n %{develname}
Summary:	%{summary} header files
Group:		Development/KDE and Qt
Requires:	libyui-devel
Requires:	%{name} = %{EVRD}
Provides:	yui-qt-devel = %{EVRD}


%description -n %{develname}
This package provides headers files for libyui-qt development.

%files -n %{develname}
%{_includedir}/yui
%{_libdir}/yui/lib*.so
%{_libdir}/cmake/libyui-ncurses
%{_libdir}/pkgconfig/libyui-ncurses.pc
%{_datadir}/libyui/buildtools/FindCurses6.cmake

#-----------------------------------------------------------------------

%prep
%autosetup -p1 -n %{name}-master

%build
./bootstrap.sh
%cmake \
    -DYPREFIX=%{_prefix}  \
    -DDOC_DIR=%{_docdir} \
    -DLIB_DIR=%{_lib}    \
    -G Ninja

%ninja_build

%install
%ninja_install -C build
