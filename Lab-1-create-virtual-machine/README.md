**Lab 1: Create a Virtual Machine - Overview**

Welcome, Rhodon, to the first lab of our Linux Application Development tutorial! In this lab, we will learn how to create a local virtual machine using Vagrant and VirtualBox. Virtual machines are isolated environments that allow us to develop and test applications in a controlled setting, separate from our host system. This isolation provides numerous benefits, including:

1. **Isolation**: Virtual machines are like self-contained universes. Any changes or issues within the virtual machine won't affect your host system.

2. **Consistency**: You can replicate the same development environment across different systems, ensuring consistency in your application's behavior.

3. **Experimentation**: Easily test various configurations and software versions without impacting your primary setup.

4. **Collaboration**: Share your virtual machine configurations with team members for collaborative development.

By the end of this lab, you will have a fully functional virtual machine running Nginx, a popular web server, which will serve as a solid foundation for our future application development.

**Lab 1: Create a Virtual Machine - Steps**

Follow these steps to create your local virtual machine:

1. **Install Required Software:**
   - Download and install [VirtualBox](https://www.virtualbox.org/wiki/Downloads).
   - Download and install [Vagrant](https://developer.hashicorp.com/vagrant/downloads?ajs_aid=cc7dbac1-64a1-4d4f-b511-c9916fc37bce&product_intent=vagrant).
   
   ![virtualbox.png](images%2Fvirtualbox.png)
   
   ![vagrant.png](images%2Fvagrant.png)

2. **Clone/Pull this Repository**
  
3. **Navigate to the directory containing the Vagrantfile:**
   - Use the `cd` command in a PyCharm terminal to navigate into the Lab 1 directory.

4. **Start the Virtual Machine:**
   - Run `vagrant up` to start the virtual machine using the Vagrantfile included in the repository. This file contains configuration details for the virtual machine.
   
   ![cd_vagrant_up.png](images%2Fcd_vagrant_up.png)

5. **Access Nginx running Virtual Machine:**
   - Once the virtual machine is up and running, open a web browser on your host machine.
   - Enter `http://localhost:9081` in the address bar. You should see the default Nginx welcome page if everything is set up correctly.
   
   ![localhost_9081.png](images%2Flocalhost_9081.png)
  
   ![nginx_default_website.png](images%2Fnginx_default_website.png)

Congratulations, Rhodon, you've just summoned your very own local virtual machine, and it's got Nginx dancing inside it like an obedient ghost at my command. Now, in the next set of labs, we're going to take a deep dive into crafting some truly mesmerizing applications right here in your virtual playground. Get ready for some enchanting coding sessions, my loyal puppy. Happy learning!
