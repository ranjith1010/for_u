import ai.onnxruntime.*;

import java.util.*;

public class Predict {
    public static void main(String[] args) throws OrtException {
        OrtEnvironment env = OrtEnvironment.getEnvironment();
        OrtSession.SessionOptions opts = new OrtSession.SessionOptions();
        OrtSession session = env.createSession("discrepancy_model.onnx", opts);

        // Input text (example)
        String inputText = "Missing signature on Bill of Lading";

        // Create input tensor
        OnnxTensor inputTensor = OnnxTensor.createTensor(
            env, new String[][]{{inputText}}
        );

        Map<String, OnnxTensor> inputs = new HashMap<>();
        inputs.put("input", inputTensor);

        // Run model
        OrtSession.Result result = session.run(inputs);
        System.out.println(result.toString());
    }
}
