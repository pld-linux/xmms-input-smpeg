Summary:	MPEG video playing plugin for XMMS
Summary(pl.UTF-8):	Wtyczka wejściowa dla XMMS-a odtwarzająca filmy MPEG
Name:		xmms-input-smpeg
Version:	0.3.5
Release:	4
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://www.xmms.org/files/plugins/smpeg-xmms/smpeg-xmms-%{version}.tar.gz
# Source0-md5:	07e49327e0d9e7f24781f29a12de94cf
Patch0:		%{name}-am15.patch
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-devel
BuildRequires:	gtk+-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	smpeg-devel >= 0.4.4
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	xmms-devel
Obsoletes:	smpeg-xmms
Obsoletes:	xmms-smpeg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This plugin allows XMMS to play MPEG movies.

%description -l pl.UTF-8
Ta wtyczka pozwala XMMS-owi odtwarzać filmy w formacie MPEG.

%prep
%setup -q -n smpeg-xmms-%{version}
%patch0 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
CPPFLAGS="-L%{_libdir}"; export CPPFLAGS
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS TODO NEWS README ChangeLog
%attr(755,root,root) %{xmms_input_plugindir}/*
