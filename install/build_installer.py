#!/usr/bin/env python3


def main():
    with open("./main.py", "r") as file:
        daemon_code = file.read()
    daemon_code = "\\n".join(daemon_code.splitlines())

    with open("./manage.sh", "r") as file:
        manager_code = file.read()
    manager_code = "\\n".join(manager_code.splitlines())
    content = (
        f"install_path='/tmp/';"
        f"echo '{daemon_code}' > $install_path/main.py;"
        f"echo '{manager_code}' > $install_path/manage.sh;"
        f"chmod +x $install_path/manage.sh $install_path/main.py;"
    )
    with open("./install/installer.sh", "w") as file:
        file.write(content)


if __name__ == "__main__":
    main()
