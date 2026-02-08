{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "ea9e77b5-327e-47f9-9507-11e091fd4aca",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "SIGTERM handler is not set because current thread is not the main thread.\n",
      "2026-02-08 07:27:11,933\tWARNING utils.py:1591 -- Python patch version mismatch: The cluster was started with:\n",
      "    Ray: 2.10.0\n",
      "    Python: 3.11.8\n",
      "This process on Ray Client was started with:\n",
      "    Ray: 2.10.0\n",
      "    Python: 3.11.14\n",
      "\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✓ Connected!\n",
      "CPUs: 14.0\n",
      "Nodes: 4\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\u001b[33m(raylet, ip=172.22.0.3)\u001b[0m [2026-02-07 23:27:15,157 E 160 190] (raylet) file_system_monitor.cc:111: /tmp/ray/session_2026-02-07_23-16-53_304182_1 is over 95% full, available space: 63615545344; capacity: 1291931721728. Object creation will fail if spilling is required.\n",
      "\u001b[33m(raylet)\u001b[0m [2026-02-07 23:27:15,289 E 251 281] (raylet) file_system_monitor.cc:111: /tmp/ray/session_2026-02-07_23-16-53_304182_1 is over 95% full, available space: 63615545344; capacity: 1291931721728. Object creation will fail if spilling is required.\n",
      "\u001b[33m(raylet, ip=172.22.0.4)\u001b[0m [2026-02-07 23:27:15,354 E 167 197] (raylet) file_system_monitor.cc:111: /tmp/ray/session_2026-02-07_23-16-53_304182_1 is over 95% full, available space: 63615541248; capacity: 1291931721728. Object creation will fail if spilling is required.\n",
      "\u001b[33m(raylet, ip=172.22.0.5)\u001b[0m [2026-02-07 23:27:15,354 E 167 197] (raylet) file_system_monitor.cc:111: /tmp/ray/session_2026-02-07_23-16-53_304182_1 is over 95% full, available space: 63615541248; capacity: 1291931721728. Object creation will fail if spilling is required.\n",
      "\u001b[33m(raylet, ip=172.22.0.3)\u001b[0m [2026-02-07 23:27:25,161 E 160 190] (raylet) file_system_monitor.cc:111: /tmp/ray/session_2026-02-07_23-16-53_304182_1 is over 95% full, available space: 63615504384; capacity: 1291931721728. Object creation will fail if spilling is required.\n",
      "\u001b[33m(raylet)\u001b[0m [2026-02-07 23:27:25,294 E 251 281] (raylet) file_system_monitor.cc:111: /tmp/ray/session_2026-02-07_23-16-53_304182_1 is over 95% full, available space: 63615504384; capacity: 1291931721728. Object creation will fail if spilling is required.\n",
      "\u001b[33m(raylet, ip=172.22.0.4)\u001b[0m [2026-02-07 23:27:25,359 E 167 197] (raylet) file_system_monitor.cc:111: /tmp/ray/session_2026-02-07_23-16-53_304182_1 is over 95% full, available space: 63615504384; capacity: 1291931721728. Object creation will fail if spilling is required.\n",
      "\u001b[33m(raylet, ip=172.22.0.5)\u001b[0m [2026-02-07 23:27:25,359 E 167 197] (raylet) file_system_monitor.cc:111: /tmp/ray/session_2026-02-07_23-16-53_304182_1 is over 95% full, available space: 63615504384; capacity: 1291931721728. Object creation will fail if spilling is required.\n",
      "\u001b[33m(raylet, ip=172.22.0.3)\u001b[0m [2026-02-07 23:27:35,165 E 160 190] (raylet) file_system_monitor.cc:111: /tmp/ray/session_2026-02-07_23-16-53_304182_1 is over 95% full, available space: 63615459328; capacity: 1291931721728. Object creation will fail if spilling is required.\n",
      "\u001b[33m(raylet, ip=172.22.0.4)\u001b[0m [2026-02-07 23:27:35,365 E 167 197] (raylet) file_system_monitor.cc:111: /tmp/ray/session_2026-02-07_23-16-53_304182_1 is over 95% full, available space: 63615459328; capacity: 1291931721728. Object creation will fail if spilling is required.\n",
      "\u001b[33m(raylet, ip=172.22.0.5)\u001b[0m [2026-02-07 23:27:35,365 E 167 197] (raylet) file_system_monitor.cc:111: /tmp/ray/session_2026-02-07_23-16-53_304182_1 is over 95% full, available space: 63615459328; capacity: 1291931721728. Object creation will fail if spilling is required.\n",
      "\u001b[33m(raylet)\u001b[0m [2026-02-07 23:27:35,299 E 251 281] (raylet) file_system_monitor.cc:111: /tmp/ray/session_2026-02-07_23-16-53_304182_1 is over 95% full, available space: 63615459328; capacity: 1291931721728. Object creation will fail if spilling is required.\n",
      "\u001b[33m(raylet, ip=172.22.0.3)\u001b[0m [2026-02-07 23:27:45,172 E 160 190] (raylet) file_system_monitor.cc:111: /tmp/ray/session_2026-02-07_23-16-53_304182_1 is over 95% full, available space: 63615422464; capacity: 1291931721728. Object creation will fail if spilling is required.\n",
      "\u001b[33m(raylet)\u001b[0m [2026-02-07 23:27:45,305 E 251 281] (raylet) file_system_monitor.cc:111: /tmp/ray/session_2026-02-07_23-16-53_304182_1 is over 95% full, available space: 63615422464; capacity: 1291931721728. Object creation will fail if spilling is required.\n",
      "\u001b[33m(raylet, ip=172.22.0.4)\u001b[0m [2026-02-07 23:27:45,370 E 167 197] (raylet) file_system_monitor.cc:111: /tmp/ray/session_2026-02-07_23-16-53_304182_1 is over 95% full, available space: 63615418368; capacity: 1291931721728. Object creation will fail if spilling is required.\n",
      "\u001b[33m(raylet, ip=172.22.0.5)\u001b[0m [2026-02-07 23:27:45,370 E 167 197] (raylet) file_system_monitor.cc:111: /tmp/ray/session_2026-02-07_23-16-53_304182_1 is over 95% full, available space: 63615418368; capacity: 1291931721728. Object creation will fail if spilling is required.\n",
      "\u001b[33m(raylet, ip=172.22.0.3)\u001b[0m [2026-02-07 23:27:55,176 E 160 190] (raylet) file_system_monitor.cc:111: /tmp/ray/session_2026-02-07_23-16-53_304182_1 is over 95% full, available space: 63615315968; capacity: 1291931721728. Object creation will fail if spilling is required.\n",
      "\u001b[33m(raylet)\u001b[0m [2026-02-07 23:27:55,311 E 251 281] (raylet) file_system_monitor.cc:111: /tmp/ray/session_2026-02-07_23-16-53_304182_1 is over 95% full, available space: 63615311872; capacity: 1291931721728. Object creation will fail if spilling is required.\n",
      "\u001b[33m(raylet, ip=172.22.0.4)\u001b[0m [2026-02-07 23:27:55,376 E 167 197] (raylet) file_system_monitor.cc:111: /tmp/ray/session_2026-02-07_23-16-53_304182_1 is over 95% full, available space: 63615311872; capacity: 1291931721728. Object creation will fail if spilling is required.\n",
      "\u001b[33m(raylet, ip=172.22.0.5)\u001b[0m [2026-02-07 23:27:55,376 E 167 197] (raylet) file_system_monitor.cc:111: /tmp/ray/session_2026-02-07_23-16-53_304182_1 is over 95% full, available space: 63615311872; capacity: 1291931721728. Object creation will fail if spilling is required.\n",
      "\u001b[33m(raylet, ip=172.22.0.3)\u001b[0m [2026-02-07 23:28:05,181 E 160 190] (raylet) file_system_monitor.cc:111: /tmp/ray/session_2026-02-07_23-16-53_304182_1 is over 95% full, available space: 63615197184; capacity: 1291931721728. Object creation will fail if spilling is required.\n",
      "\u001b[33m(raylet)\u001b[0m [2026-02-07 23:28:05,316 E 251 281] (raylet) file_system_monitor.cc:111: /tmp/ray/session_2026-02-07_23-16-53_304182_1 is over 95% full, available space: 63615197184; capacity: 1291931721728. Object creation will fail if spilling is required.\n",
      "\u001b[33m(raylet, ip=172.22.0.4)\u001b[0m [2026-02-07 23:28:05,381 E 167 197] (raylet) file_system_monitor.cc:111: /tmp/ray/session_2026-02-07_23-16-53_304182_1 is over 95% full, available space: 63615193088; capacity: 1291931721728. Object creation will fail if spilling is required.\n",
      "\u001b[33m(raylet, ip=172.22.0.5)\u001b[0m [2026-02-07 23:28:05,381 E 167 197] (raylet) file_system_monitor.cc:111: /tmp/ray/session_2026-02-07_23-16-53_304182_1 is over 95% full, available space: 63615193088; capacity: 1291931721728. Object creation will fail if spilling is required.\n",
      "\u001b[33m(raylet, ip=172.22.0.3)\u001b[0m [2026-02-07 23:28:15,187 E 160 190] (raylet) file_system_monitor.cc:111: /tmp/ray/session_2026-02-07_23-16-53_304182_1 is over 95% full, available space: 63615143936; capacity: 1291931721728. Object creation will fail if spilling is required.\n",
      "\u001b[33m(raylet)\u001b[0m [2026-02-07 23:28:15,322 E 251 281] (raylet) file_system_monitor.cc:111: /tmp/ray/session_2026-02-07_23-16-53_304182_1 is over 95% full, available space: 63615135744; capacity: 1291931721728. Object creation will fail if spilling is required.\n",
      "\u001b[33m(raylet, ip=172.22.0.5)\u001b[0m [2026-02-07 23:28:15,387 E 167 197] (raylet) file_system_monitor.cc:111: /tmp/ray/session_2026-02-07_23-16-53_304182_1 is over 95% full, available space: 63615135744; capacity: 1291931721728. Object creation will fail if spilling is required.\n",
      "\u001b[33m(raylet, ip=172.22.0.4)\u001b[0m [2026-02-07 23:28:15,387 E 167 197] (raylet) file_system_monitor.cc:111: /tmp/ray/session_2026-02-07_23-16-53_304182_1 is over 95% full, available space: 63615135744; capacity: 1291931721728. Object creation will fail if spilling is required.\n",
      "\u001b[33m(raylet, ip=172.22.0.3)\u001b[0m [2026-02-07 23:28:25,194 E 160 190] (raylet) file_system_monitor.cc:111: /tmp/ray/session_2026-02-07_23-16-53_304182_1 is over 95% full, available space: 63615041536; capacity: 1291931721728. Object creation will fail if spilling is required.\n",
      "\u001b[33m(raylet)\u001b[0m [2026-02-07 23:28:25,328 E 251 281] (raylet) file_system_monitor.cc:111: /tmp/ray/session_2026-02-07_23-16-53_304182_1 is over 95% full, available space: 63615041536; capacity: 1291931721728. Object creation will fail if spilling is required.\n",
      "\u001b[33m(raylet, ip=172.22.0.5)\u001b[0m [2026-02-07 23:28:25,394 E 167 197] (raylet) file_system_monitor.cc:111: /tmp/ray/session_2026-02-07_23-16-53_304182_1 is over 95% full, available space: 63615041536; capacity: 1291931721728. Object creation will fail if spilling is required.\n",
      "\u001b[33m(raylet, ip=172.22.0.4)\u001b[0m [2026-02-07 23:28:25,394 E 167 197] (raylet) file_system_monitor.cc:111: /tmp/ray/session_2026-02-07_23-16-53_304182_1 is over 95% full, available space: 63615041536; capacity: 1291931721728. Object creation will fail if spilling is required.\n",
      "\u001b[33m(raylet, ip=172.22.0.3)\u001b[0m [2026-02-07 23:28:35,199 E 160 190] (raylet) file_system_monitor.cc:111: /tmp/ray/session_2026-02-07_23-16-53_304182_1 is over 95% full, available space: 63614959616; capacity: 1291931721728. Object creation will fail if spilling is required.\n",
      "\u001b[33m(raylet)\u001b[0m [2026-02-07 23:28:35,334 E 251 281] (raylet) file_system_monitor.cc:111: /tmp/ray/session_2026-02-07_23-16-53_304182_1 is over 95% full, available space: 63614959616; capacity: 1291931721728. Object creation will fail if spilling is required.\n",
      "\u001b[33m(raylet, ip=172.22.0.4)\u001b[0m [2026-02-07 23:28:35,399 E 167 197] (raylet) file_system_monitor.cc:111: /tmp/ray/session_2026-02-07_23-16-53_304182_1 is over 95% full, available space: 63614959616; capacity: 1291931721728. Object creation will fail if spilling is required.\n",
      "\u001b[33m(raylet, ip=172.22.0.5)\u001b[0m [2026-02-07 23:28:35,399 E 167 197] (raylet) file_system_monitor.cc:111: /tmp/ray/session_2026-02-07_23-16-53_304182_1 is over 95% full, available space: 63614959616; capacity: 1291931721728. Object creation will fail if spilling is required.\n",
      "\u001b[33m(raylet, ip=172.22.0.3)\u001b[0m [2026-02-07 23:28:45,205 E 160 190] (raylet) file_system_monitor.cc:111: /tmp/ray/session_2026-02-07_23-16-53_304182_1 is over 95% full, available space: 63614873600; capacity: 1291931721728. Object creation will fail if spilling is required.\n",
      "\u001b[33m(raylet)\u001b[0m [2026-02-07 23:28:45,340 E 251 281] (raylet) file_system_monitor.cc:111: /tmp/ray/session_2026-02-07_23-16-53_304182_1 is over 95% full, available space: 63614873600; capacity: 1291931721728. Object creation will fail if spilling is required.\n",
      "\u001b[33m(raylet, ip=172.22.0.5)\u001b[0m [2026-02-07 23:28:45,405 E 167 197] (raylet) file_system_monitor.cc:111: /tmp/ray/session_2026-02-07_23-16-53_304182_1 is over 95% full, available space: 63614873600; capacity: 1291931721728. Object creation will fail if spilling is required.\n",
      "\u001b[33m(raylet, ip=172.22.0.4)\u001b[0m [2026-02-07 23:28:45,405 E 167 197] (raylet) file_system_monitor.cc:111: /tmp/ray/session_2026-02-07_23-16-53_304182_1 is over 95% full, available space: 63614869504; capacity: 1291931721728. Object creation will fail if spilling is required.\n",
      "\u001b[33m(raylet, ip=172.22.0.3)\u001b[0m [2026-02-07 23:28:55,211 E 160 190] (raylet) file_system_monitor.cc:111: /tmp/ray/session_2026-02-07_23-16-53_304182_1 is over 95% full, available space: 63614767104; capacity: 1291931721728. Object creation will fail if spilling is required.\n",
      "\u001b[33m(raylet)\u001b[0m [2026-02-07 23:28:55,347 E 251 281] (raylet) file_system_monitor.cc:111: /tmp/ray/session_2026-02-07_23-16-53_304182_1 is over 95% full, available space: 63614763008; capacity: 1291931721728. Object creation will fail if spilling is required.\n",
      "\u001b[33m(raylet, ip=172.22.0.4)\u001b[0m [2026-02-07 23:28:55,411 E 167 197] (raylet) file_system_monitor.cc:111: /tmp/ray/session_2026-02-07_23-16-53_304182_1 is over 95% full, available space: 63614763008; capacity: 1291931721728. Object creation will fail if spilling is required.\n",
      "\u001b[33m(raylet, ip=172.22.0.5)\u001b[0m [2026-02-07 23:28:55,408 E 167 197] (raylet) file_system_monitor.cc:111: /tmp/ray/session_2026-02-07_23-16-53_304182_1 is over 95% full, available space: 63614763008; capacity: 1291931721728. Object creation will fail if spilling is required.\n"
     ]
    }
   ],
   "source": [
    "import ray\n",
    "\n",
    "ray.init(\n",
    "    address='ray://ray-head:10001',\n",
    "    namespace='lattice-detection'\n",
    ")\n",
    "\n",
    "print(\"✓ Connected!\")\n",
    "print(f\"CPUs: {ray.available_resources()['CPU']}\")\n",
    "print(f\"Nodes: {len(ray.nodes())}\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ef4117e4-3be6-4a75-a30e-020630c7b7ab",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.14"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
