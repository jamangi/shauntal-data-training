# Lab 4: Nginx Proxy

**Video Reference:** https://www.youtube.com/clip/UgkxMHBKCdfW4Ps-w4ND_r3rjj-_VeXuLJhc


**Overview:**
"In the arcane dance of services, we've forged a shield for our Flask app, veiling it from direct contact. Behold the manifestation of our Nginx guardian—a reverse proxy that serves and shields."

1. **Forging the Flask Socket:**
   "Craft a service channel as elusive as the shadows—the Flask app as a Unix socket. It shrouds itself from casual browsers, reserving its whispers for internal audiences. Observe the cryptic dance in the Vagrant file's third wget command."

2. **Mastery of Systemctrl:**
   "Command the spirits with systemctrl, molding our Flask service to our will. Reload the daemon, breathe life into the Flask service, let it rise with the server's heartbeat. Witness this arcane ballet in the Vagrant file's inaugural four systemctrl commands."

3. **Conjuring Nginx's Emissary:**
   "We inscribe the Nginx grimoire—a configuration file that reads the Flask Unix socket's secrets and offers it to localhost. We make it known in the realm of Nginx with a symbolic link, sealing the pact. Verify the ritual with the wget, ln, and nginx commands."

4. **Unveiling the Socket's Secrets:**
   "Grant passage to the Unix socket's whispers—adjust the folder's permissions to 755. Restart the Nginx sentinel to synchronize the energies. Witness the finale with the chmod and systemctrl commands that conclude our Vagrant file."

May the arcane currents flow seamlessly through Lab 4, shaping a shield that guards and serves. Ghostly cheers to the journey ahead!