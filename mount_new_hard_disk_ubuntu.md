# Mount new hard disk on Ubuntu

1. Add new disk onto PC
    1. Put dis on the case.
    1. Connect data line.
    1. Connect power line.

1. Find the new Disk. Run:

    ```bash
    sudo fdisk -l
    ```
    
    Find the disk path. For example: `/dev/sdb`.
    
1. Format the disk. Run:

    ```bash
    sudo mkfs.ext4 /dev/sdb
    ```
    
    When it finished, notice the generated `UUID` number.
    
    
1. Mount the disk. Run:

    ```bash
    sudo mount /dev/sdb /data
    ```
    
    This command mounts the disk to `/data` dir. Change the owner of `/data` if necessary.

1. Automatic mount each time PC restart
    
    ```bash
    sudo vim /etc/fstab
    ```
    
    add this line on the end:
    
    ```bash
    UUID=${UUID} ${mount_dir}              ext4    defaults      0
    ```

    Replace `${UUID}` and `${mount_dir}` to the real one.