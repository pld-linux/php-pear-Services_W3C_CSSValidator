%define		status		alpha
%define		pearname	Services_W3C_CSSValidator
Summary:	%{pearname} - An Object Oriented Interface to the W3C CSS Validator service
Summary(pl.UTF-8):	%{pearname} - zorientowany obiektowo interfejs do usługi walidacji CSS
Name:		php-pear-%{pearname}
Version:	0.2.3
Release:	1
License:	BSD
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	ad89f426eb4e28c889db7e42d5f1a1b5
URL:		http://pear.php.net/package/Services_W3C_CSSValidator/
BuildRequires:	php-pear-PEAR >= 1:1.5.4
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php-pear
Requires:	php-pear-HTTP_Request2 >= 0.2.0
Obsoletes:	php-pear-Services_W3C_CSSValidator-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides an object oriented interface to the API of the
W3 CSS Validator application (http://jigsaw.w3.org/css-validator/).
With this package you can connect to a running instance of the
validator and retrieve the validation results (true|false) as well as
the errors and warnings for a a style sheet.

By using the SOAP 1.2 output format from the validator, you are
returned simple objects containing all the information from the
validator.

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
Pakiet ten udostępnia zorientowanego obiektowo interfejsu do API
usługi kontroli poprawności CSS serwisu W3C
(http://jigsaw.w3.org/css-validator/). Przy użyciu tego pakietu
możliwe jest podłączenie się do instancji walidatora i pobranie wyniku
kontroli poprawności (prawda|fałsz) jak również komunikatów błędów i
ostrzeżeń dla danego arkusza stylów.

Poprzez wykorzystanie formatu SOAP 1.2, w wyniku zwracane są proste
obiekty zawierające wszystkie informacje walidatora.

Ta klasa ma w PEAR status: %{status}.

%prep
%pear_package_setup

mv ./usr/share/pear/data/Services_W3C_CSSValidator/README .
mv docs/Services_W3C_CSSValidator/docs/examples .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log README
%{php_pear_dir}/.registry/*.reg
%dir %{php_pear_dir}/Services/W3C
%{php_pear_dir}/Services/W3C/CSSValidator
%{php_pear_dir}/Services/W3C/CSSValidator.php
%{_examplesdir}/%{name}-%{version}
