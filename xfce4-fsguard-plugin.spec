Summary:	A fsguard plugin for the Xfce panel
Summary(pl.UTF-8):	Wtyczka fsguard dla panelu Xfce
Name:		xfce4-fsguard-plugin
Version:	0.3.0
Release:	1
License:	BSD
Group:		X11/Applications
Source0:	http://goodies.xfce.org/releases/xfce4-fsguard-plugin/%{name}-%{version}.tar.bz2
# Source0-md5:	27770ad4c4b737bfb0f3fb2457b33729
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-fsguard-plugin
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	intltool >= 0.35.0
BuildRequires:	xfce4-dev-tools >= 4.4.0
BuildRequires:	xfce4-panel-devel >= 4.4.0
Requires:	xfce4-panel >= 4.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The fsguard plugin checks free space on a chosen mount point
frequently and displays an alarm if free space is less than given
alarm limit.

%description -l pl.UTF-8
Wtyczka fsguard sprawdza czêsto wolne miejsce na wybranym punkcie
montowania i wy¶wietla alarm je¶li jest mniej miejsca ni¿ zadany
limit.

%prep
%setup -q

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

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/xfce4/panel-plugins/xfce4-fsguard-plugin
%{_datadir}/xfce4/panel-plugins/fsguard.desktop
