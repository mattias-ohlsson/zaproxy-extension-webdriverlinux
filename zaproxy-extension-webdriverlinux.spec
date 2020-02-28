%global extension_id webdriverlinux
%global extension_name Linux WebDrivers
%global extension_info Linux WebDrivers for Firefox and Chrome.
%global extension_infoUrl /docs/desktop/addons/linux-webdrivers/
%global addon_folder webdrivers/%{extension_id}

Name:           zaproxy-extension-%{extension_id}
Version:        17
Release:        1%{?dist}
Summary:        %{extension_name} extension

License:        ASL 2.0
URL:            https://www.zaproxy.org%{extension_infoUrl}
Source0:        https://github.com/zaproxy/zap-extensions/archive/%{extension_id}-v%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  java-11-openjdk-headless
Requires:       zaproxy

%description
%{extension_info}

%prep
%autosetup -n zap-extensions-%{extension_id}-v%{version}

%build
JAVA_HOME=/usr/lib/jvm/jre-11-openjdk ./gradlew :addOns:$(echo %{addon_folder} | tr / :):build

%install
rm -rf $RPM_BUILD_ROOT
install -d -m 755 %{buildroot}%{_datadir}/zaproxy/plugin
install -m 644 addOns/%{addon_folder}/build/zapAddOn/bin/*-%{version}.zap \
 %{buildroot}%{_datadir}/zaproxy/plugin

%files
%license LICENSE
%doc README.md CONTRIBUTING.md addOns/%{addon_folder}/CHANGELOG.md
%{_datadir}/zaproxy/plugin/*-%{version}.zap

%changelog
* Fri Feb 28 2020 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 17-1
- Update to 17

* Wed Feb 26 2020 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 16-1
- Initial build
