Name:	google-authenticator-pam	
Version:	1.0
Release:	1%{?dist}
Summary:	Google Authenticator Pam Modules
Group:		System Environment/Base
License:	Apache License 2.0
URL:		https://code.google.com/p/google-authenticator
Source0:	google-authenticator-pam-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	pam-devel	
Requires:	pam	

%description

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
#rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc

%changelog
