if __name__ == "__main__":
    versions = ["2.5", "2.6", "2.7", "3.2", "3.3", "3.4", "3.5", "3.6", "3.7", "3.8"]
    with open("build_containers.sh", "w") as file:
        for version in versions:
            file.write(
                f"fetchy dockerize --distribution ubuntu --version bionic --exclude exclusions.txt --ppa deadsnakes --tag fetchy/python:{version} --out packages-{version} python{version}\n"
            )
            file.write("rm -rf extracted\n")
    with open("push_containers.sh", "w") as file:
        for version in versions:
            file.write(f"docker push fetchy/python:{version}\n")
    with open("verify_containers.sh", "w") as file:
        for version in versions:
            string_to_print = f'"Succesfully built image for {version}"'
            file.write(
                f"docker run fetchy/python:{version} python{version} -c 'print({string_to_print})'\n"
            )
