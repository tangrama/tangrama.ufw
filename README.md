# Tangrama: UFW

Role to install *ufw* package and configure it.

## Packages

This role install the *ufw* package.

## Role Variables

### additional_ports

List additional ports that should accept connections.

```yaml
    additional_ports:
        - 80
        - 443
```

## Example Playbook

```yaml
    - hosts: servers
      roles:
         - { role: tangrama.ufw }
      vars:
        additional_ports:
            - 80
            - 443
```

### ssh_port

Port number to be used by *sshd* process.

```yaml
    ssh_port: 9923
```

## Example Playbook

```yaml
    - hosts: servers
      roles:
         - { role: tangrama.ufw }
      vars:
        ssh_port: 9923
```

## Testing

This role uses [molecule](https://molecule.readthedocs.io/) for linting and testing.

```shell
    molecule test
```

## License

GPLv2

## Author Information

* Tangrama Team, Tangrama.
