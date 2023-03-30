# Create an SSH configuration file using Puppet
include stdlib

file_line{'Set Identity file location':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => '  IdentityFile ~/.ssh/school',
  replace => true
}

file_line{'Disable password authentication':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => '  PasswordAuthentication no',
  replace => true
}
