Name:           hello-doc
Version:        1.2
Release:        1%{?dist}
Summary:        Hello Doc project to test CI/CD pipeline

License:        GPLv3+
URL:            https://gitlab.com/nqb1/%{name}
Source0:        https://gitlab.com/nqb1/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildRequires:  make
BuildRequires:  asciidoctor

Requires:       httpd

BuildArch:      noarch

%description


%prep
%setup -q


%build
make %{?_smp_mflags}


%install
# TO REMOVE ? propose a fix
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%license LICENSE
/var/www/html/README.html
%doc


%changelog
* Fri Nov 16 2018 Nicolas Quiniou-Briand <nqb@inverse.ca> - 1.1-1
- First hello-doc package
