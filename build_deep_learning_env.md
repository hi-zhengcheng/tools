# Build deep learning Env

# 1. Hardware



Type|Item
:----|:----
**CPU** | [Intel - Xeon E5-1630 V4 3.7GHz Quad-Core OEM/Tray Processor](https://pcpartpicker.com/product/cxVD4D/intel-xeon-e5-1630-v4-37ghz-quad-core-oemtray-processor-cm8066002395300)
**CPU Cooler** | [Corsair - H100i v2 70.7 CFM Liquid CPU Cooler](https://pcpartpicker.com/product/CrDzK8/corsair-cpu-cooler-cw9060025ww)
**Motherboard** | [Asus - ROG STRIX X99 GAMING ATX LGA2011-3 Motherboard](https://pcpartpicker.com/product/L6rcCJ/asus-motherboard-rogstrixx99gaming)
**Memory** | [Corsair - Vengeance LPX 16GB (1 x 16GB) DDR4-2666 Memory](https://pcpartpicker.com/product/PntWGX/corsair-memory-cmk16gx4m1a2666c16)
**Storage** | [Samsung - 970 Pro 512GB M.2-2280 Solid State Drive](https://pcpartpicker.com/product/thvbt6/samsung-970-pro-512gb-m2-2280-solid-state-drive-mz-v7p512bw)
**Storage** | [Seagate - Barracuda 2TB 3.5" 7200RPM Internal Hard Drive](https://pcpartpicker.com/product/CbL7YJ/seagate-barracuda-2tb-35-7200rpm-internal-hard-drive-st2000dm006)
**Case** | [Corsair - 780T ATX Full Tower Case](https://pcpartpicker.com/product/sNJwrH/corsair-case-cc9011063ww)
**Power Supply** | [Corsair - HX Platinum 1200W 80+ Platinum Certified Fully-Modular ATX Power Supply](https://pcpartpicker.com/product/f7L7YJ/corsair-hx-platinum-1200w-80-platinum-certified-fully-modular-atx-power-supply-cp-9020140-na)

# 2. Software

### 1. Ubuntu 18.04

* [Create bootable USB driver on mac os](https://itsfoss.com/create-bootable-ubuntu-usb-drive-mac-os/)

### 2. GPU driver

* Install it through **Software & Updates** tools in Ubuntu.

### 3. tensorflow

* Docker make life easier. It only needs Nvidia GUI driver installed in the host machine. All the other things are included in **tensorflow docker image**. Follow the [tensorflow docker install guide](https://www.tensorflow.org/install/docker).

# 3. Docker commands

1. Help:
    ```
    docker image --help
    docker container --help
    ```

1. View Images:
    ```
    docker images
    ```

1. Run one image:
    ```
    docker run hello-world
    ```
    * Once you run one **image**, you create one **container**.
    * Container has two status: running, stopped.

1. View running containers:
    ```
    docker ps
    docker container ls
    ```

1. View all containers:
    ```
    docker container ls -a
    ```

1. Remove one stopped container:
    ```
    docker container ls -a
    docker container rm ${containerID}
    ```

1. Remove all stopped container:
    ```
    docker container prune
    ```

1. Docker run options:
    ```
    --rm : Automatically remove the container when it exits
    -it : interactive, Allocate a pseudo-TTY
    -p hostPort:containerPort : map port number, can have one or more
    -v hostFolder:containerFolder : map directory
    --name ${some_name} : give container one name
    --runtime=nvidia : specify nvidia-docker
    --detach : Run container in background and print container ID
    ```

1. Stop one container:
    ```
    docker stop ${containerID}
    ```

1. Restart one container:
    ```
    docker start ${containerID}
    ```
    * Restarted container has the same options when created by run the image.

# 4. Docker workflow

1. Run image first time:
    ```
    docker run \
        --runtime=nvidia \
        -p ${port_in_host_pc}:${port_in_docker} \
        -v ${dir_in_host_pc}:${dir_in_docker} \
        -w ${work_dir_in_docker} \
        --detach \
        --name tf-1.11.0 \
        tensorflow/tensorflow:1.11.0-gpu
    ```
    * It will create one container. Reuse the created container later.

1. Check:
    ```
    docker ps
    ```

1. Start one shell in docker env
    ```
    docker exec -it -u ${uid}:${gid} ${container_id} bash
    ```
    * It's OK to exit this shell whenever you like.

1. Stop container:
    ```
    docker stop ${container_id}
    ```

1. Restart one container:
    ```
    docker container ls -a
    docker start ${container_id}
    ```

1. Remove useless container:
    ```
    docker rm ${docker_id}
    ```

1. View container's detail information
    ```
    docker inspect ${docker_id}
    ```
    * Can find information like dir mapping.

# 5. Unsolved problem:

1. Tensorflow in docker uses **Root** user. It's OK but not good. I tried this [user map](https://www.jujens.eu/posts/en/2017/Jul/02/docker-userns-remap/#id2) method, but eventually failed to start tensorflow.
