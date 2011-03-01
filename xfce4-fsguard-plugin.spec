Summary:	A fsguard plugin for the Xfce panel
Summary(pl.UTF-8):	Wtyczka fsguard dla panelu Xfce
Name:		xfce4-fsguard-plugin
Version:	1.0.0
Release:	2
License:	BSD
Group:		X11/Applications
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-fsguard-plugin/1.0/%{name}-%{version}.tar.bz2
# Source0-md5:	8378f922b59a0d5a378af5e45a18c4a3
Patch0:		%{name}-ui.patch
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-fsguard-plugin
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	intltool >= 0.35.5
BuildRequires:	libxfce4ui-devel
BuildRequires:	rpmbuild(macros) >= 1.601
BuildRequires:	xfce4-dev-tools >= 4.4.0
BuildRequires:	xfce4-panel-devel >= 4.4.0
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Requires:	xfce4-panel >= 4.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The fsguard plugin checks free space on a chosen mount point
frequently and displays an alarm if free space is less than given
alarm limit.

%description -l pl.UTF-8
Wtyczka fsguard sprawdza często wolne miejsce na wybranym punkcie
montowania i wyświetla alarm jeśli jest mniej miejsca niż zadany
limit.

%prep
%setup -q
%patch0 -p1

%build
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/ur_PK

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/xfce4-fsguard-plugin
%{_datadir}/xfce4/panel-plugins/fsguard.desktop
%{_iconsdir}/hicolor/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.svg
