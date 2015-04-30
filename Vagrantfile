VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.network "forwarded_port", guest: 80, host: 8080 #forward 80 from guest to local machine port 8080
  
  config.vm.provision :ansible do |ansible|
    ansible.playbook = "wordpress.yml"
  end
  
end
