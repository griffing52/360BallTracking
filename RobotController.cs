using System.Collections;
using System.Collections.Generic;
using System;
using System.IO;
using System.Net.Sockets;
using System.Text;
using UnityEngine;

public class RobotController : MonoBehaviour
{
	// class RobotPose {
	// 	public double? X { get; set; }
    //     public double? Y { get; set; }
    //     public double? Rot { get; set; }
	// }

	internal Boolean socketReady = false;

	TcpClient socket;
	NetworkStream stream;
	StreamReader reader;
	StreamWriter writer;
	private String HOST = "127.0.0.1";
	private Int32 PORT = 65432;


	private Vector3 center;

	public Vector3 Coordinate3d;
	public Vector3 Rotation;

    // Start is called before the first frame update
    void Start()
    {
		setupSocket();
        Coordinate3d = new Vector3(0, 0.791f, 0);
        Rotation = new Vector3(0, 0, 0);
		center = gameObject.GetComponent<Renderer>().bounds.center;
		writeSocket("ping");
    }

    // Update is called once per frame
    void Update()
    {
		string line = readSocket();
		if (line != "") {
			try {
				string[] vals = line.Split(',');
				Coordinate3d.x = float.Parse(vals[0]);
				Coordinate3d.z = float.Parse(vals[1]);
				Rotation.y = -float.Parse(vals[2]);
				gameObject.transform.position = Coordinate3d;
				gameObject.transform.eulerAngles =  Rotation;
			} catch (Exception e) {
				Debug.Log(line + " :Read error: " + e);
			}
			
			// gameObject.transform.RotateAround()
			// gameObject.transform.Rotate(0, float.Parse(vals[2]), 0, Space.World);
			// gameObject.transform.Rotate(0, float.Parse(vals[2]), 0);
		}
		writeSocket("ping");
    }

	public void setupSocket() {
		try {
			socket = new TcpClient(HOST, PORT);
			stream = socket.GetStream();
			reader = new StreamReader(stream);
			writer = new StreamWriter(stream);
			stream.ReadTimeout = 1;
			socketReady = true;
		} catch (Exception e) {
			Debug.Log("Socket error: " + e);
		}
	}

	public void writeSocket(string arg) {
		if (!socketReady)
			return;
		string complete_line = arg + "\n\r";
		try {
			writer.Write(complete_line);
			writer.Flush();
		} catch (Exception e) {
			Debug.Log("Writer error: " + e);
		}
	}

	public string readSocket() {
		if (!socketReady) {
			Debug.Log("Socket not ready: ");
			return "";
		}
		Byte[] data = new Byte[256];

		// String to store the response ASCII representation.
		String responseData = String.Empty;

		// Read the first batch of the TcpServer response bytes.
		// try {
		Int32 bytes = stream.Read(data, 0, data.Length);
		responseData = System.Text.Encoding.ASCII.GetString(data, 0, bytes);
		// Console.WriteLine("Received: {0}", responseData);
		return responseData;
		// } catch (Exception e) {

		// 	return "";
		// }
	}
}




// using System.Collections;
// using System.Collections.Generic;
// using System;
// using System.IO;
// using System.Net.Sockets;
// using System.Text;
// using System.Web.Script.Serialization;
// using UnityEngine;

// public class RobotController : MonoBehaviour
// {
// 	class RobotPose {
// 		public double? X { get; set; }
//         public double? Y { get; set; }
//         public double? Rot { get; set; }
// 	}
// 	StreamReader reader;

// 	public Vector3 Coordinate3d;

//     // Start is called before the first frame update
//     void Start()
//     {
// 		setupSocket();
//         Coordinate3d = new Vector3(0, 0, 0);
//     }

//     // Update is called once per frame
//     void Update()
//     {
// 		gameObject.transform.position = Coordinate3d;
//     }

// 	public string readSocket() {
// 		if (!socketReady) {
// 			Debug.Log("Socket not ready: ");
// 			return "";
// 		}
// 		return reader.ReadLine();
// 	}
// }