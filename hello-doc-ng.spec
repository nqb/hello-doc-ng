Name:           hello-doc-ng
Version:        1.8
Release:        1%{?dist}
Summary:        Hello Doc project to test CI/CD pipeline

License:        GPLv3+
URL:            https://gitlab.com/nqb1/%{name}
Source0:        https://gitlab.com/nqb1/%{name}/-/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  ruby
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
* Thu Dec 06 2018 nqb <nqb@users.noreply.github.com> 1.7-1
- new package built with tito

* Wed Dec 05 2018 Nicolas Quiniou-Briand <nqb@inverse.ca> - 1.6-1
- Ruby dependency
* Wed Dec 05 2018 Nicolas Quiniou-Briand <nqb@inverse.ca> - 1.4-1
- Last fix before a great build
* Wed Dec 05 2018 Nicolas Quiniou-Briand <nqb@inverse.ca> - 1.3-2
- Remove 'v' from git tags
* Wed Dec 05 2018 Nicolas Quiniou-Briand <nqb@inverse.ca> - 1.3-1
- Fix issue with tar format in upstream sources
* Fri Nov 16 2018 Nicolas Quiniou-Briand <nqb@inverse.ca> - 1.1-1
- First hello-doc package
