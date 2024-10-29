import requests
import argparse


API_URL = "http://127.0.0.1:5000"
SHARED_KEY = ""


def create_contact(first_name, last_name, company, mobile_list, email, note):
    contact_data = {
        "first_name": first_name,
        "last_name": last_name,
        "company": company,
        "mobile_list": mobile_list,
        "email": email,
        "note": note,
    }
    response = requests.post(f"{API_URL}/create", json=contact_data)
    print(response.json())


def edit_contact(
    resource_name, first_name, last_name, company, mobile_list, email, note
):
    contact_data = {
        "resource_name": resource_name,
        "first_name": first_name,
        "last_name": last_name,
        "company": company,
        "mobile_list": mobile_list,
        "email": email,
        "note": note,
    }
    response = requests.put(f"{API_URL}/edit", json=contact_data)
    print(response.json())


def delete_contact(resource_name):
    response = requests.delete(
        f"{API_URL}/delete", json={"resource_name": resource_name}
    )
    print(response.json())


def main():
    parser = argparse.ArgumentParser(description="Manage Google Contacts.")
    parser.add_argument(
        "--token-path", required=True, help="Path to the JSON token file"
    )
    subparsers = parser.add_subparsers(dest="operation", help="Operation to perform")

    # Create sub-command
    create_parser = subparsers.add_parser("create", help="Create a new contact")
    create_parser.add_argument(
        "--first-name", required=True, help="First name of the contact"
    )
    create_parser.add_argument(
        "--last-name", required=True, help="Last name of the contact"
    )
    create_parser.add_argument(
        "--company", required=False, help="Company of the contact"
    )
    create_parser.add_argument(
        "--mobile", nargs="+", required=True, help="Mobile number of the contact"
    )
    create_parser.add_argument(
        "--email", required=False, help="Email address of the contact"
    )
    create_parser.add_argument("--note", required=False, help="Note about the contact")

    # Edit sub-command
    edit_parser = subparsers.add_parser("edit", help="Edit an existing contact")
    edit_parser.add_argument("resource_name", help="ID of the contact to edit")
    edit_parser.add_argument(
        "--first-name", required=True, help="First name of the contact"
    )
    edit_parser.add_argument(
        "--last-name", required=True, help="Last name of the contact"
    )
    edit_parser.add_argument("--company", required=False, help="Company of the contact")
    edit_parser.add_argument(
        "--mobile", nargs="+", required=True, help="Mobile number of the contact"
    )
    edit_parser.add_argument(
        "--email", required=False, help="Email address of the contact"
    )
    edit_parser.add_argument("--note", required=False, help="Note about the contact")

    # Delete sub-command
    delete_parser = subparsers.add_parser("delete", help="Delete an existing contact")
    delete_parser.add_argument("resource_name", help="ID of the contact to delete")

    args = parser.parse_args()

    if args.operation == "create":
        create_contact(
            args.first_name,
            args.last_name,
            args.company,
            args.mobile,
            args.email,
            args.note,
        )
    elif args.operation == "edit":
        try:
            edit_contact(
                args.resource_name,
                args.first_name,
                args.last_name,
                args.company,
                args.mobile,
                args.email,
                args.note,
            )
        except:
            print(0)
    elif args.operation == "delete":
        try:
            delete_contact(args.resource_name)
        except:
            print(0)


if __name__ == "__main__":
    main()
