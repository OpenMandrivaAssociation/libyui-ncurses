%define major 8
%define libname %mklibname yui %{major}-ncurses
%define develname %mklibname yui-ncurses -d

Name:		libyui-ncurses
Version:	2.52.0
Release:	1
Summary:	UI abstraction library - Ncurses plugin
License:	LGPLv2+
Group:		System/Libraries
Url:		https://github.com/libyui/libyui-ncurses
Source0:	https://github.com/libyui/libyui-ncurses/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:		libyui-ncurses-compile-workaround.patch

BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libyui) >= 3.1.2
BuildRequires:	pkgconfig(ncursesw)
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	qmake5
BuildRequires:	boost-devel
BuildRequires:	doxygen
#BuildRequires:	texlive
BuildRequires:	graphviz
BuildRequires:	ghostscript
BuildRequires:	pkgconfig(fontconfig)
Requires:	libyui

%description
%{summary}.

#-----------------------------------------------------------------------

%package -n %{libname}
Summary:	%{summary}
Group:		System/Libraries
Requires:	libyui
Requires:	%{_lib}qt5x11extras5
Provides:	%{name} = %{EVRD}
Provides:	libyui%{major}-ncurses = %{EVRD}

%description -n %{libname}
This package contains the library needed to run programs
dynamically linked with libyui-ncurses.

%files -n %{libname}
%{_libdir}/yui/lib*.so.*

#-----------------------------------------------------------------------

%package -n %{develname}
Summary:	%{summary} header files
Group:		Development/KDE and Qt
Requires:	libyui-devel
Requires:	%{name} = %{EVRD}
Provides:	yui-ncurses-devel = %{EVRD}

%description -n %{develname}
This package provides headers files for libyui-ncurses development.

%files -n %{develname}
%{_includedir}/yui
%{_libdir}/yui/lib*.so
%{_libdir}/cmake/libyui-ncurses
%{_libdir}/pkgconfig/libyui-ncurses.pc
%{_datadir}/libyui/buildtools/FindCurses6.cmake

#-----------------------------------------------------------------------

%package -n %{name}-tools
Summary:        Libyui-ncurses tools
Group:      System/Libraries
# conflict with libyui-ncurses8, /usr/bin/libyui-terminal was originally there
Conflicts:  %{mklibname yui 8-ncurses} < 2.43.9-3
Requires:   screen

%description -n %{name}-tools
Character based (ncurses) user interface component for libYUI.
libyui-terminal - useful for testing on headless machines

%files -n %{name}-tools
%{_bindir}/libyui-terminal

#-----------------------------------------------------------------------

%prep
%autosetup -p1

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
