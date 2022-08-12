# install Flask 

package {'Flask':
ensure   => '2.1.0',
provider => 'pip3',
#source   => '/usr/lib/python3/dist-packages',
}
