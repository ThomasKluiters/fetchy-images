if __name__ == "__main__":
    parameters = [
        "1.8",
        "1.9",
        "1.10",
        "1.11",
        "1.12"
    ]
    with open("build_containers.sh", "w") as file:
        for version in parameters:
            file.write(
                f"fetchy dockerize --ppa longsleep/golang-backports --distribution ubuntu --codename bionic --tag fetchy/golang:{version} golang-{version} --exclude golang-{version}-doc\n"
            )
    with open("push_containers.sh", "w") as file:
        for version in parameters:
            file.write(f"docker push fetchy/golang:{version}\n")
