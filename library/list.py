from ansible.module_utils.basic import *

def main():
    fields = {
        "hello": {"default": True, "type": "str"},
        "ourlist": {"default": True, "type": "list"}
    }

    module = AnsibleModule(argument_spec=fields)
    # updating the vars
    module.params.update({"hello": "Hello World Now"})
    new_list = [1,2,3,4,5,6]
    module.params.update({"ourlist":new_list})
    
    module.exit_json(changed=True, meta= module.params)

if __name__ == '__main__':
    main()