if __name__ == "__main__":
    parameters = [
        ("7", "ubuntu", "trusty"),
        ("8", "ubuntu", "xenial"),
        ("11", "ubuntu", "bionic")
    ]
    with open("build_containers.sh", "w") as file:
        for (version, distro, codename) in parameters:
            file.write(
                f"fetchy dockerize --distribution {distro} --codename {codename} --exclude exclusions.txt --tag fetchy/java:{version} openjdk-{version}-jre-headless\n"
            )
    with open("push_containers.sh", "w") as file:
        for (version, distro, codename) in parameters:
            file.write(f"docker push fetchy/java:{version}\n")
    with open("verify_containers.sh", "w") as file:
        for (version, distro, codename) in parameters:
            file.write(
                f"docker run fetchy/java:{version} java -v'\n"
            )
